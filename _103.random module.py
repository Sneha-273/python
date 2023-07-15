from numpy import random
z=random.rand()#returns float value in 0-1 range
x=random.rand(7)
a=random.randint(10,size=(3))#returns intger value
b=random.randint(50,size=(2,4))
print("float value:\n",z)
print("shape of array:\n",x)
print("1D array:\n",a)
print("2D array:\n",b)