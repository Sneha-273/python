import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
sb.distplot(random.logistic(loc=2,scale=2,size=100),hist=False)
mlt.show()