import numpy as np
a=np.array([[1,2,3,4,'*'],[0,'+',5,7,8]])
print(a.shape)
#shape:returns (dimension,total item)
#reshape:allows to changes its dimensions
arr=np.array([11,22,33,55,77,890,44,3,4,6,9,7,5,6,98,87,90,0])
new_arr=arr.reshape(3,6)
print(new_arr)