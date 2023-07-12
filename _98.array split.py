#spliting:separetes the given array
import numpy as np
a=np.array([0,1,2,3,4,5,6,7])
a1=np.array_split(a,1)
a2=np.array_split(a,2)
a3=np.array_split(a,6)
print(a1)
print(a2)
print(a3)
print("\n")
#hsplit ,vsplit , dsplit are all opposite of hstack ,vstack ,dstack
b=np.array([[1,2],[2,3],[4,5]])
b1=np.hsplit(b,2)
print(b1)