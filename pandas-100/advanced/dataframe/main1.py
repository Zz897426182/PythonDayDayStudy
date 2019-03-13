#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})
print(df)
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
print(df)
temp = df['From_To'].str.split('_', expand=True)
temp.columns = ['From', 'To']
print(temp)
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
print(temp)

df = df.drop('From_To', axis=1)
df = df.join(temp)
print(df)

df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
print(df)

delays = df['RecentDelays'].apply(pd.Series)
delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns) + 1)]
print(delays)
df = df.drop('RecentDelays', axis=1).join(delays)
print(df)