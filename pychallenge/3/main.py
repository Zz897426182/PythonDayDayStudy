#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
import string
from functools import reduce

""" regex """
text = open('character.txt').read()
result = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))
print(result)

""" string """
s = open('character.txt').read()
lwr = string.ascii_lowercase
upr = string.ascii_uppercase
aa = [s[n + 3] for n in range(1, len(s) - 7)
      if (s[n - 1] in lwr) and (s[n] in upr) and (s[n + 1] in upr) \
      and (s[n + 2] in upr) and (s[n + 3] in lwr) \
      and (s[n + 4] in upr) and (s[n + 5] in upr) \
      and (s[n + 6] in upr) and (s[n + 7] in lwr)]
print(*aa, sep='')

""" reduce """


def level_3(state, c):
    if not c.isalpha():
        return state
    if state:
        chars_found, state_lower, upper_count = state
    else:
        state_lower = ""
        upper_count = 0
        chars_found = ""
    if c.islower():
        if upper_count == 3:
            if state_lower:
                chars_found += state_lower
            state_lower = c
        else:
            state_lower = ""

        upper_count = 0
    else:
        upper_count += 1
    return chars_found, state_lower, upper_count


with open('character.txt') as f:
    s = f.read()
    s += "x"
    print(reduce(level_3, s, ())[0])
