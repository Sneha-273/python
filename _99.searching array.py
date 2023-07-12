#where():use to search certain data
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,8,4,5,2,8,9])
b=np.where(a==2)
c=np.where(a%2==0)
print(b)
print(c)