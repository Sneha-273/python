#concatenate():use for joinig two arrays in one array with its "axis"
import numpy as np
a1=np.array([["@",33,"*",2],[1,2,3,4]])
a2=np.array([['a','b'],[0,0]])
x=np.concatenate((a1,a2),axis=1)
print(x)
