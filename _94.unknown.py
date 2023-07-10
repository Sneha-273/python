import numpy as np
a=np.array([1,2,3,45,6,7,8,9])
na=a.reshape(2,2,-1)
print(na)
print("----------------")
b=np.array([[[0,9],[2,3],[5,6]]])
nb=b.reshape(-1)#flattening the array
print(nb)