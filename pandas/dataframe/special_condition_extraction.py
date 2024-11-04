import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df = DataFrame(data)

#　条件（フィルター）
print(df[df['City'] == 'Tokyo'])

# 'Birth_year'が1990以上かつ1995未満
print(df[(df['Birth_year'] >= 1990) & (df['Birth_year'] < 1995)])

#　'City'が'Tokyo'または'Osaka'
print(df[df['City'].isin(['Tokyo','Osaka'])])