import numpy as n
a=n.array("A")
d=n.array(['a','b'])#ndarray:its a array objrct supports numpy
b=n.array([[0,1,2],[1,0,2]])
c=n.array([[[0,0,0],[1,1,1],[2,2,2]]])
print("0 dimensional array:\n",a)
print("1 dimensional array:\n",d)
print("2 dimensional array:\n",b)
print("3 dimensional array:\n",c)
#ndim: returns the integer number of dimentions
print(a.ndim)
print(b.ndim)
print(d.ndim)
print(c.ndim)