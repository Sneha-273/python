#stack():use to joining two arrays in way in stacking
import numpy as np
a=np.array(['@','@','*',"*"])
b=np.array(['$','^','^','~'])
x=np.stack((a,b),axis=1)
print(x)
print("\n")
#hstack():arrange array in one row
y=np.hstack((a,b))
print(y)
#vstack():arrange array in columns
print('\n')
z=np.vstack((a,b))
print(z)
#dstack():arrange height same as depth
print('\n')
q=np.dstack((a,b))
print(q)