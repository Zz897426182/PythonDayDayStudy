#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import string

text = open('mess.txt').read()
def my_solution(text):
    s = list(filter(lambda x: x in string.ascii_letters, text))
    print(*s, sep='')

if __name__ == '__main__':
    my_solution(text)

s = ''.join([line.rstrip() for line in open('mess.txt')])
occ = {}
for c in s:
    occ[c] = occ.get(c, 0) + 1
    avgOc = len(s) // len(occ)
print(''.join([c for c in s if occ[c] < avgOc]))
