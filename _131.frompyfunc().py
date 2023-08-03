import numpy as np
def my_add(a,b,c):
    return a+b+c
my_add=np.frompyfunc(my_add,3,1)  #frompyfunc(funtion name,input/no.of array,output/no.of output array

print(my_add([0,0],[1,1],[2,2]))
print(type(np.add))
print(type(np.concatenate))