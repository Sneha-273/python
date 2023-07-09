#base: let you know the array own data or not
import numpy as np
x=np.array([2,3,4,5,6])
a=x.copy()
b=x.view()
print(a.base)
print(b.base)