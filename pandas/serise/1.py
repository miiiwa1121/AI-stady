import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

series = Series([1,1,0,6,2,3,14])
print(series)

series_i = Series([1,1,0,6,2,3,14],index=['a', 'b', 'c', 'd', 'e', 'f','g'])
print(series_i)
print('要素:', series_i.values)
print('インデックス:', series_i.index)