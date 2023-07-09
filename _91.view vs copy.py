#copy():owns the data ,doesn't effct on original data
#view():not owns data , any changes make different view
import numpy as nm
a=nm.array([1,2,3,4,5,6,7,8])
z=a.copy()
a[0]=99#new data get added and old data get vanished but in copy its the same
print(a)
print(z)
print("----------------------")
b=nm.array([9,8,7,6,5])
c=b.view()#make changes on both side
b[0]=100
print(b)
print(c)