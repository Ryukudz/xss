#!/usr/bin/env python3
import sys
import requests
import argparse
from rich import print

tested_parameters = set()
vulnerable_urls = []

def xss_test(url, value, parameter, payload):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "X-Bounty-Hunter": "bug-bounty-hunter"
    }

    target = url.replace(value, payload)

    try:
        response = requests.get(target, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return

    print(f"[blue ][~][green bold] testing [yellow]\"{parameter}\"[white]: {target}")

    if payload in response.text:
        print(f"[green][✓][yellow bold] \"{parameter}\"[white] is[red bold] Vulnerable[white]: {target}")
        vulnerable_urls.append(target)

def process_url(url, payload):
    if '?' in url:
        params = url.split('?')[1].split('&')
        for param in params:
            param_value_pair = param.split('=')
            if len(param_value_pair) == 2:
                parameter, value = param_value_pair
            elif len(param_value_pair) == 1:
                parameter = param_value_pair[0]
                value = ''
            else:
                continue

            if parameter not in tested_parameters:
                tested_parameters.add(parameter)
                xss_test(url, value, parameter, payload)

def main():
    parser = argparse.ArgumentParser(description='Finds low hanging fruit XSS 😱')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the URLs wordlist.')
    parser.add_argument('-s', '--silent', action='store_true', help="Won't print the banner.")
    parser.add_argument('-p', '--payload', type=str, default='<img src="x">', help='Payload to use. Default: <img src="x">')
    args = parser.parse_args()

    if not args.silent:
        print("\n[white] Coded by [blue bold]ryuku 🥷\n")

    urls = []
    if not sys.stdin.isatty():
        # Read URLs from stdin
        urls = sys.stdin.read().splitlines()
    elif args.wordlist:
        with open(args.wordlist, 'r') as f:
            urls = f.readlines()

    for url in urls:
        process_url(url, args.payload)

    if vulnerable_urls:
        print("\n[red bold]Findings:")
        for url in vulnerable_urls:
            print(url)
    else:
        print("\n[red bold][!][blue italic] No findings 💀.\n[white]Remember that this script tests only for reflected XSS and it's not 100% accurate make sure to retest manually later on.")

if __name__ == '__main__':
    main()
