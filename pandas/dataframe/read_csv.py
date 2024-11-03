import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

#student-mat.csvファイルをDataFrameオブジェクトとして読み込まれる
# student_data_math = pd.read_csv('C:\Python\GCI-winter-2024\pandas\include\student-mat.csv')
# print(student_data_math.head())

# カンマで区切ってデータを読む
student_data_math = pd.read_csv('C:\Python\GCI-winter-2024\pandas\include\student-mat.csv', sep=';')
print(student_data_math.head())
