import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df_i2 = DataFrame(data,index=['e','b','a','d','c'])
# print(df_i2)

# indexによるソート
print(df_i2.sort_index())

# 値によるソート:ascendingを指定で降順
print(df_i2.sort_values(by='Birth_year', ascending=False))