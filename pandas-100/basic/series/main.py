#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# print(pd.__version__)

arr = [0, 1, 2, 3,4]
s1= pd.Series(arr)
s1.index=['A', 'B', 'C', 'D', 'E']
# print(s1)

n = np.random.randn(5)
index = ['a', 'b', 'c', 'd', 'e']
s2 = pd.Series(n, index=index)
# print(s2)

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s3 = pd.Series(d)
# print(s3)

s4 = s3.append(s1)
# print(s4)

s4 = s4.drop('e')

# print(s4)

s4['A'] = 6
# print(s4)

# print(s4['B'])

# print(s4[:3])

# print(s4.add(s3))
# print(s4.sub(s3))
print(s4.median)