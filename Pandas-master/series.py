import numpy as np
import pandas as pd

# series = pd.Series()
# print(series)

arr1 = np.array([1,22,12,414,14,13,254,16,73])
series1 = pd.Series(arr1)
print(series1)

arr2 = np.array({'a':1,'b':22, 'd':10, 'c':6})
series2 = pd.Series(arr2)
print(series2)
print(series1[2:4])
