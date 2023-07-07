#[start:end:step]
import numpy as np
a=np.array(['a','b',1,2,3,'z'])
print(a[0:2])
print(a[:4])
print(a[-5:-1])
print(a[1:7:2])
print(a[::3])
