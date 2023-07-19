#premutation : arrangement of element
from numpy import random
import numpy as np
a=np.array(["@",3,6,"*",0])
random.shuffle(a)#change original array
print(a)
print(random.shuffle(a))
print("\n")
b=np.array([1,2,3,4,5])
print(random.permutation(b))#unchange original array also re-arrange array
print(b)