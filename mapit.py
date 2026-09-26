#!/usr/bin/env python3
"""
mapit.py - Launches a map in the browser using an address from the command line or clipboard.
"""

import webbrowser
import urllib.parse
import sys

import pyperclip

BASE_URL = 'https://maps.apple.com/?q='
# BASE_URL = 'https://www.google.com/maps/search/?api=1&query='


def main():
    if len(sys.argv) > 1:
        # get address from the comamand line
        address = ' '.join(sys.argv[1:])
    else:
        # get the address from the clipboard
        address = pyperclip.paste().strip()

    if not address:
        print('usage: mapit: <address>    (or copy an address to the clipboard first)', file=sys.stderr)
        sys.exit(1)

    webbrowser.open(BASE_URL + urllib.parse.quote_plus(address))

if __name__ == "__main__":
    main()