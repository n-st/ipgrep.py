#!/usr/bin/env python3

import fileinput
import ipaddress
import unicodedata


EXCLUDED_PUNCTUATION_CHARS = ['.', ':']


def is_delimiter(char):
    if char in EXCLUDED_PUNCTUATION_CHARS:
        return False
    cat = unicodedata.category(char)
    # Space_Separator or *_Punctuation or *_Control
    return cat == 'Zs' or cat.startswith('P') or cat.startswith('C')


def parse(s):
    try:
        addr = ipaddress.ip_address(s)
        print(addr)
    except:
        # So the word wasn't an IP itself. Let's see if there were any excess
        # punctuation chars at either of its ends...
        recheck = []
        if s[-1] in EXCLUDED_PUNCTUATION_CHARS:
            recheck += [s[0:-1]]
        if s[0] in EXCLUDED_PUNCTUATION_CHARS:
            recheck += [s[1:]]
        if s[0] in EXCLUDED_PUNCTUATION_CHARS and s[-1] in EXCLUDED_PUNCTUATION_CHARS:
            recheck += [s[1:-1]]

        for r in recheck:
            try:
                addr = ipaddress.ip_address(r)
                print(addr)
            except:
                pass


for line in fileinput.input():
    charlist = list(line)
    word = []
    while charlist:
        char = charlist.pop(0)
        if is_delimiter(char):
            if word:
                parse(''.join(word))
            word = []
        else:
            word.append(char)

    if word:
        parse(''.join(word))

