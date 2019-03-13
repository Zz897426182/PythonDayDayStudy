#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(12).reshape(6, 2), index=[list('AAABBB'), list('123123')],
                     columns=['hello', 'shiyanlou'])
# print(numpy.arange(12).reshape(6, 2))
# print(frame)
frame.index.names = ['first', 'second']
# print(frame)

# print(frame.groupby('first').sum())

# print(frame)
# frame.stack()

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# df = pd.DataFrame(data, index=labels)
# print(df['age'] > 3)
# print(df[df['age'] > 3])
# print(df.iloc[2:4, 1:3])
# print(df[(df['animal'] == 'cat') & (df['age'] < 3)])
# print(df[df['animal'].isin(['cat', 'dog'])])
# print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])
# print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
# print(df['priority'].map({'yes': True, 'no': False}))
# print(df.groupby('animal').sum())

temp_df1 = pd.DataFrame(np.random.randn(5, 4))
temp_df2 = pd.DataFrame(np.random.randn(5, 4))
temp_df3 = pd.DataFrame(np.random.randn(5, 4))

# print(temp_df1)
# print(temp_df2)
# print(temp_df3)

pieces = [temp_df1, temp_df2, temp_df3]
# print(pd.concat(pieces))

# df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
# print(df)
# print(df.sum())
# print(df.sum().idxmin())
# print(df.sum().idxmax())

# df = pd.DataFrame(np.random.random(size=(5, 3)))
# print(df)
# print(df.sub(df.mean(axis=1), axis=0))

# df = pd.DataFrame({'A': list('aaabbcaabcccbbc'), 'B': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
#
# print(df)
# print(df.groupby('A')['B'].nlargest(3).sum(level=0))

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
# print(df)
# print(pd.pivot_table(df, index=['A', 'B']))
# print(pd.pivot_table(df, values=['D'], index=['A', 'B']))
# print(pd.pivot_table(df, values=['D'], index=['A', 'B'], aggfunc=[np.sum, len]).to_excel('123.xlsx'))
# print(pd.pivot_table(df, values=['D'], index=['A', 'B'], columns=['C'], aggfunc=np.sum).to_excel('123.xlsx'))
#
# print(pd.pivot_table(df, values=['D'], index=['A','B'], columns=['C'], aggfunc=np.sum, fill_value=0))
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": [
    'a', 'b', 'b', 'a', 'a', 'e']})
print(df)
df['grade'] = df['raw_grade'].astype('category')
print(df)
df['grade'].cat.categories = ['very good', 'good', 'very bad']
# print(df)
df['grade'] = df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])
print(df)

print(df.sort_values(by='grade'))

print(df.groupby('grade').size())

