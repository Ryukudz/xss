# XSS 🪟

automate the process of finding reflected XSS using this script.

## Installation ⚙️

```sh
git clone https://github.com/Ryukudz/xss
cd xss
pip install -r requirements.txt
```

## Usage 🪄
Examples:
```
python3 xss.py -w targets.txt
echo "https://example.com/index.html?name=test" | python3 xss.py
```
Help:
```sh
python3 xss.py -h
```

This will display help for the tool

```yaml
usage: xss.py [-h] [-w WORDLIST] [-s] [-p PAYLOAD]

Finds low hanging fruit XSS 😱

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Path to the URLs wordlist.
  -s, --silent          Won't print the banner.
  -p PAYLOAD, --payload PAYLOAD
                        Payload to use. Default: <img src="x">
```
