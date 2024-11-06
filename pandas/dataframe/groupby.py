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

city_map ={
    'Tokyo': 'Kanto',
    'Hokkaido': 'Hokkaido',
    'Osaka': 'Kansai',
    'Kyoto':'Kansai'
}

df1['region'] = df1['city'].map(city_map)

# print(df1)

# サイズ情報
# print(df1.groupby('city').size())

# cityを軸に、birth_yearの平均値を求める
# print(df1.groupby('city')['birth_year'].mean())

# region、cityを2軸として、birth_yearの平均値
# print(df1.groupby(['region', 'city'])['birth_year'].mean())

# as_index = Falseパラメータを設定すると、インデックスが設定されなくなります。
# print(df1.groupby(['region', 'city'], as_index = False)['birth_year'].mean())

# for group, subdf in df1.groupby('region'):
#     print('==========================================================')
#     print('Region Name:{0}'.format(group))
#     print(subdf)

student_data_math = pd.read_csv('GCI-winter-2024\pandas\include\student-mat.csv', sep = ';')

# 列に複数の関数を適応
functions = ['count','mean','max','min']
grouped_student_math_data1 = student_data_math.groupby(['sex','address'])
print(grouped_student_math_data1[['age','G1']].agg(functions))