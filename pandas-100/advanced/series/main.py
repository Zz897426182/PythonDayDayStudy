#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy
import pandas

# dti = pandas.date_range(start='2018-01-01', end='2018-12-31', freq='D')
# s = pandas.Series(numpy.random.rand(len(dti)), index=dti)

# print(s[s.index.weekday == 2].sum())
# print(s.resample('M').mean())

# s = pandas.date_range('today', periods=100, freq='S')
# ts = pandas.Series(numpy.random.randint(0, 500, len(s)), index=s)
# print(ts.resample('Min').sum())

# s = pandas.date_range('today', periods=1, freq='D')
# ts = pandas.Series(numpy.random.randn(len(s)), s)
# ts_utc = ts.tz_localize('UTC')
# print(ts_utc)
# print(ts_utc.tz_convert('Asia/Shanghai'))

# rng = pandas.date_range('1/1/2018', periods=5, freq='M')
# ts = pandas.Series(numpy.random.randn(len(rng)), index=rng)
# print(ts)
# ps = ts.to_period()
# print(ps)
# print(ps.to_timestamp())

letters = ['A', 'B', 'C']
numbers = list(range(10))
mi = pandas.MultiIndex.from_product([letters, numbers])
s = pandas.Series(numpy.random.rand(30), index=mi)
# print(s.loc['A', [1, 3, 6]])
print(s.loc[pandas.IndexSlice[:'B', 5:]])