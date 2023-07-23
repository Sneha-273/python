import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
sb.distplot(random.normal(loc=20,scale=5,size=100),hist=False)
sb.distplot(random.poisson(lam=20,size=1000),hist=False)
mlt.show()