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

#　分割の粒度
birth_year_bins = [1980, 1985, 1990, 1995, 2000]

# ビン分割の実施
birth_year_cut_data = pd.cut(df1.birth_year, birth_year_bins)
# print(birth_year_cut_data)

# 集計結果
# print(pd.value_counts(birth_year_cut_data))

# 名前をつける
group_names = ['early1980s', 'late1980s', 'early1990s', 'late1990s']
birth_year_cut_data = pd.cut(df1.birth_year, birth_year_bins, labels = group_names)
# print(pd.value_counts(birth_year_cut_data))


# 数字で分割数指定可能。ここでは2つに分割
# print(pd.cut(df1.birth_year, 2))

#分位点での分割
print(pd.value_counts(pd.qcut(df1.birth_year, 4)))