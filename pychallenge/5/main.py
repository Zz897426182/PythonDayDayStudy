#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pickle

class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

data = pickle.load(StrToBytes(open('banner.p', 'rb')))

for each in data:
    print(each)