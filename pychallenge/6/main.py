#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
img = Image.open('oxygen.png')
row = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 7)]
print(*row, sep='')