import numpy as np
a=np.array([[1,2,3],['a','b','c']])
row=int(input("enter the row number:"))
col=int(input("enter the column number:"))
print("the position on",row,"and position on ",col,"is:",a[row,col])