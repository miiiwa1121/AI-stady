import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df = DataFrame(data)

df_i = DataFrame(data,index=['a','b','c','d','e'])

print(df.T)#行と列を入れ替える
print('/n')

# print(df['Birth_year'])#列名の指定（1つの場合）
# このように記述することも可能
# print(df.Birth_year)

# 列名の指定(複数の場合)
# print(df[['ID', 'Birth_year']])

# 新しい列の作成
# df['Score'] = np.arange(5)*10
# print(df)

# 行名の指定
# print(df[0:3])

# 行名の指定
print(df_i['a':'c'])