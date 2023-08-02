#zipf:nth number have 1/n chance
import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
x=random.zipf(a=3,size=100)
sb.distplot(x[x<5],hist=True)
mlt.show()