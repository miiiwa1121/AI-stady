import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

data = {'ID':['100','101','102','103','104'],
            'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
            'Birth_year':[1990,1989,1992,1997,1982],
            'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

df = DataFrame(data)

# print(df)

# データの列の削除
# print(df.drop(['Birth_year'], axis = 1))

# データの行の削除
# print(df.drop(index=[0,2]))

# 3列3行のデータを作成し、インデックスとカラムを設定
hier_df= DataFrame(
    np.arange(9).reshape((3,3)),
    index = [
        ['a','a','b'],
        [1,2,2]
    ],
    columns = [
        ['Osaka','Tokyo','Osaka'],
        ['Blue','Red','Red']
    ]
)
# print(hier_df)

# indexに名前を付ける
hier_df.index.names =['key1','key2']

# カラムに名前を付ける
hier_df.columns.names =['city','color']
# print(hier_df)

#カラムの絞り込み
# print(hier_df['Osaka'])

# 階層ごとの要約統計量：行合計
# print(hier_df.groupby(level= 'key2', axis = 0).sum())

# 列平均
# print(hier_df.groupby(level= 'color', axis = 1).mean())

# インデックスの要素の削除
# print(hier_df.drop(['b']))

#　ピボット操作で「Blue、Red」の列を行に変更
# print(hier_df.stack())

# unstackメソッドで、「Blue、Red」の行を列に変更
print(hier_df.stack().unstack())