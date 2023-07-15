#in a filtering boolean index list use and only true values have existing in new array and
#false values get ignored
import numpy as np
z=np.array([1,2,3,4])
a=[True,True,False,False]
print(z[a])
