# データの準備
import numpy as np
from numpy import nan as NA
import pandas as pd

df = pd.DataFrame(np.random.rand(10, 4))

# NAにする
df.iloc[1,0] = NA
df.iloc[2:3,2] = NA # 行2のみが選択されます。スライス[2:3]は終了インデックス3が含まれないため、df.iloc[2, 2]と同じ。
df.iloc[5:,3] = NA

# print(df)

# リストワイズ削除:NaNがある行をすべて取り除く
# print(df.dropna())

# ペアワイズ削除:使いたい列を取り出してからdropnaメソッドを適用
# print(df[[0,1]].dropna())

# fillna:NaNになっている箇所をある値で埋める
# print(df.fillna(0))

# 直前の行の値で埋める
# print(df.fillna(method = 'ffill'))

# 各カラムの平均値(確認用)
# print(df.mean())

# 平均値で埋める
print(df.fillna(df.mean()))
