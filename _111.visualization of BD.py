import matplotlib.pyplot as mlt
import  seaborn as sb
from numpy import random
sb.distplot(random.binomial(n=5,p=0.5,size=100),hist=True,kde=False)
mlt.show()