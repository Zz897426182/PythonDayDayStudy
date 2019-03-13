#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

dates = pd.date_range('today', periods=6)
num_arr = np.random.randn(6, 4)
columns = ['A', 'B', 'C', 'D']
df1 = pd.DataFrame(num_arr, index=dates, columns=columns)
# #print(df1)

dasta = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(dasta, index=labels)
# #print(df2)
# #print(df2.dtypes)

df3 = df2.copy()

num = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index=df3.index)
df3['No.'] = num
# print(df3)
# print(df3.iat[1, 0])
df3.loc['f', 'age'] = 1.5
# print(df3)
# print(df3.mean())

string = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
# print(string)
# print(string.str.lower())

df4 = df3.copy()
# print(df4)
# print(df4.fillna(value=3))

df5 = df3.copy()
# print(df5)
# print(df5.dropna(how='any'))

left = pd.DataFrame({'key': ['foo1', 'foo2'], 'one': [1, 2]}, index=['a', 'b'])
right = pd.DataFrame({'key': ['foo2', 'foo3'], 'two': [4, 5]}, index=['c', 'd'])
# print(left)
# print('\n')
# print(right)
# print('\n')
#
# print(pd.merge(left, right, on='key'))

# df3.to_csv('animal.csv')
# df_animal = pd.read_csv('animal.csv')
# print(df_animal)
# print(df_animal[0:1])

df3.to_excel('animal.xlsx', sheet_name='Sheet1')