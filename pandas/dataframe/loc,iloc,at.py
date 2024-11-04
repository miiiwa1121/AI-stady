import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df = DataFrame(data)

# 行名の指定（1つの場合）
# print(df.loc[2])

# 行名の指定（複数の場合）
# print(df.loc[0:3])

# 列名の指定（1つの場合）
# print(df.loc[:, 'Birth_year'])

# 列名の指定（複数の場合）
# print(df.loc[:, ['ID','Birth_year']])

# 0から3行かつ'ID'または'Birth_year'の列を指定
# print(df.loc[0:3, ['ID','Birth_year']])

#iloc:0から4つ目・loc:0から4まで
# print(df.iloc[0:4])
# print(df.loc[0:4])

# 0から3行かつ'ID'または'Birth_year'の列を指定
# print(df.iloc[0:4, [0,2]])

# 0行目の'ID'を取得
# print(df.at[0,'ID'])

# df.loc[],df.iloc[],df.at[],df.iat[]は=を用いて値を代入
df.at[0,'Birth_year'] = 2000
print(df)