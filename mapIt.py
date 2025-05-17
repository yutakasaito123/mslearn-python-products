#!/usr/local/bin/python3

import webbrowser, sys, pyperclip
if (len(sys.argv)) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('Address:', address)

webbrowser.open('https://www.google.com/maps/place/' + address)

#  コンテナではpyperclipが使えない
