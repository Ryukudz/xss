import requests
import argparse
import concurrent.futures
from rich import print

def xss_test(url, value, payload):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "X-Bounty-Hunter": "bug-bounty-hunter"
    }

    target = url.replace(value, payload)

    try:
        response = requests.get(target, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[red][✖] [white bold]{e}")
        return

    print(f"[blue ][~][green bold] testing[white]: {target}")

    if payload in response.text:
        print(f"[green][✓][red bold] Vulnerable[white]: {target}")

def process_url(url, payload):
    if '?' in url:
        params = url.split('?')[1].split('&')
        for param in params:
            param_value_pair = param.split('=')
            if len(param_value_pair) == 2:
                _, value = param_value_pair
            elif len(param_value_pair) == 1:
                value = ''
            else:
                continue
            xss_test(url, value, payload)

def main():
    parser = argparse.ArgumentParser(description='Finds low hanging fruit XSS 😱')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the URLs wordlist.')
    parser.add_argument('-s', '--silent', action='store_true', help="Won't print the banner.")
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads to use. Default: 10')
    parser.add_argument('-p', '--payload', type=str, default='<img src="x">', help='Payload to use. Default: <img src="x">')
    args = parser.parse_args()

    if not args.silent:
        print("\n[white] Coded by [blue bold]ryuku 🥷\n")

    with open(args.wordlist, 'r') as f:
        urls = f.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(process_url, urls, [args.payload] * len(urls))

if __name__ == '__main__':
    main()
