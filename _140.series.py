#series:columns,1D array
import pandas as pd
a=[4,5,6,7,8,9]
print(pd.Series(a))
print('\n')
print(pd.Series(a,index=['a','b','c','e','f','g']))