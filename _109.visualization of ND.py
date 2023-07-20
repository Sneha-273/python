import matplotlib.pyplot as mt
import seaborn as sb
from numpy import random
sb.distplot(random.normal(size=10),hist=False)
mt.show()