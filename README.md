# XSS 🪟

automate the process of finding reflected XSS using this script.

## Installation ⚙️

```sh
git clone https://github.com/Ryukudz/xss
cd xss
pip install -r requirements.txt
```

## Usage 🪄

```sh
python3 xss.py -h
```

This will display help for the tool, Here are all the switches it supports.

```yaml
usage: xss.py [-h] [-w WORDLIST] [-s] [-t THREADS] [-p PAYLOAD]

Finds low hanging fruit XSS 😱

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Path to the URLs wordlist.
  -s, --silent          Won't print the banner.
  -t THREADS, --threads THREADS
                        Number of threads to use. Default: 10
  -p PAYLOAD, --payload PAYLOAD
                        Payload to use. Default: <img src="x">
```
