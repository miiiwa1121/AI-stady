import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data1 = {
    'id': ['100', '101', '102', '103', '104', '106', '108', '110', '111',' 113'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'birth_year': [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steeve', 'Mituru', 'Aoi', 'Tarou', 'Suguru','Mitsuo']
}
df1 = DataFrame(data1)
print(df1)

data2 = {
    'id': ['100', '101', '102', '105', '107'],
    'math': [50, 43, 33, 76, 98],
    'english': [90, 30, 20, 50, 30],
    'sex': ['M','F','F','M','M'],
    'index_num': [0, 1, 2, 3, 4]
}
df2 = DataFrame(data2)
print(df2)

data3 = {
    'id': ['117', '118', '119', '120', '125'],
    'city': ['Chiba', 'Kanagawa', 'Tokyo', 'Fukuoka', 'Okinawa'],
    'birth_year': [1990, 1989, 1992, 1997, 1982],
    'name': ['Suguru', 'Kouichi', 'Satochi', 'Yukie', 'Akari']
}
df3 = DataFrame(data3)
print(df3)

# データのマージ（内部結合。キーは自動的に認識される:id）
# print(pd.merge(df1, df2))

# データのマージ（内部結合。onで明示的に指定可能）
# print(pd.merge(df1, df2, on = 'id'))

# Indexとindex_num によるマージ
# print(pd.merge(df1, df2, left_index = True, right_on = 'index_num'))

# suffixesを指定:同じ名前が衝突したときに付加される文字を設定できる
# print(pd.merge(df1, df2, left_index = True, right_on = 'index_num', suffixes=('_1','_2')))

# 左外部結合:ひとつめの引数に合わせて結合/データがふたつめの引数にない場合は、NaN
# print(pd.merge(df1, df2, how = 'left'))

# 完全外部結合:どちらかのデータに存在する列で結合
# print(pd.merge(df1, df2, how = 'outer'))

# concat 縦結合
# print(pd.concat([df1,df3]))

# ignore_index=True:上から順番にindexを付け直す
# print(pd.concat([df1, df3], ignore_index=True))

# sort引数 : True:Columnが並べ替えらる / False:並べ替えられない
# print(pd.concat([df1, df2], sort=True))

# 横に結合
print(pd.concat([df1, df2], axis=1))