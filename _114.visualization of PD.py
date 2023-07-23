import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
sb.distplot(random.exponential(scale=2,size=100),hist=False)
mlt.show()