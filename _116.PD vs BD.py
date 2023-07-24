import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
sb.distplot(random.binomial(n=10,p=0.5,size=1000),hist=False,label='binomial')
sb.distplot(random.poisson(lam=10,size=1000),hist=False,label='poission')
mlt.show()