import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import random
sb.distplot(random.rayleigh(scale=10,size=(100)),hist=False)
mlt.show()