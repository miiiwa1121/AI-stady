import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

# print(data)
df = DataFrame(data)#dataをDataFrame形式に変換
# print(df)

print(df.head())#先頭n文字出力

df_i = DataFrame(data,index=['a','b','c','d','e'])
print(df_i)