import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

#　重複があるデータ
dupli_data = DataFrame({
        'col1': [1, 1, 2, 3, 4, 4, 6, 6],
        'col2': ['a', 'b', 'b', 'b', 'c', 'c', 'b', 'b']
})
print('・元のデータ')
print(dupli_data)

#　重複判定
print(dupli_data.duplicated())

#　重複削除
print(dupli_data.drop_duplicates())