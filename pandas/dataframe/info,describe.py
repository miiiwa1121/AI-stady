import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

student_data_math = pd.read_csv('C:\Python\GCI-winter-2024\pandas\include\student-mat.csv', sep=';')

# すべてのカラムの情報等チェック
# student_data_math.info()

# 基本統計量をチェック
print(student_data_math.describe())