#random distribution :set of random numbers that follows PDF
#probbility distribution functions describes continuous probability
from numpy import random
a=random.choice(["*","$",1,2,3],p=[0.2,0.2,0.3,0.1,0.2],size=(2,3))
print(a)                       #p is predefined make sure pobability sum 1