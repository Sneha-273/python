import numpy as n
a=n.array([[0,'*',10,110],['@',2,3,4]])
print(a)
print(a[0,1:3])
#row num ^ ,^slice
print(a[0:3,2])
#row num:end,column
print("->",a[0:2,1:3])
#row num:row num,start:end