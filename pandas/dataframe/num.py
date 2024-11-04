import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df_i2 = DataFrame(data)
# print(df_i2)

# 値があるかどうかの確認
print(df_i2.isin(['Tokyo','Osaka']))

# 欠損値の取り扱い
# name をすべてnanにする
# isnull:nanかどうかを判定
df_i2['Name'] = np.nan
# print(df_i2.isnull())

# sum:nullを判定し、合計する
print(df_i2.isnull().sum())