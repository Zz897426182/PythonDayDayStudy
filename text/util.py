#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def lines(file):
    for line in file:
        yield ord(line)
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

if __name__ == '__main__':
    aa = 'aaeeebaa1a2a3b'
    print(aa.strip('ab'))