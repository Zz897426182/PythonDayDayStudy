#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.DataFrame({'name': ['Alice', 'Bob', 'Candy', 'Dany', 'Ella',
#                             'Frank', 'Grace', 'Jenny'], 'grades': [58, 83, 79, 65, 93, 45, 61, 88]})
# def choice(x):
#     if x > 60:
#         return 1
#     else:
#         return 0
#
# df.grades = pd.Series(map(lambda x: choice(x), df.grades))
#
# print(df)

# df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
# print(df['A'].shift())
# print(df.loc[df['A'].shift() != df['A']])
# print(df.drop_duplicates())

# def normalization(df):
#     numerator = df.sub(df.min())
#     denominator = (df.max().sub(df.min()))
#     Y = numerator.div(denominator)
#     return Y
#
# df = pd.DataFrame(np.random.random(size=(5, 3)), index=['a', 'b', 'c', 'd', 'e'])
# print(df)
# print(normalization(df))
# %matplotlib inline
# ts = pd.Series(np.random.randn(100), index=pd.date_range('today', periods=100))
# ts = ts.cumsum()
# ts.plot()
#
# df = pd.DataFrame(np.random.randn(100, 4), index=ts.index,
#                   columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
# df.plot()
# plt.show()

# df = pd.DataFrame({'xs': [1, 5, 2, 8, 1], 'ys': [4, 2, 1, 9, 6]})
# df = df.cumsum()
# df.plot.scatter('xs', 'ys', color = 'red', marker='*')
# plt.show()

df = pd.DataFrame({"revenue": [57, 68, 63, 71, 72, 90, 80, 62, 59, 51, 47, 52],
                   "advertising": [2.1, 1.9, 2.7, 3.0, 3.6, 3.2, 2.7, 2.4, 1.8, 1.6, 1.3, 1.9],
                   "month": range(12)
                   })
ax = df.plot.bar("month", "revenue", color="yellow")
df.plot('month', 'advertising', secondary_y=True, ax=ax)
plt.show()


