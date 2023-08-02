import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
sb.distplot(random.pareto(a=2,size=1000),hist=False)
mlt.show()