#uniform: equal chance
from numpy import random
import matplotlib.pyplot as mlt
import seaborn as sb
z=random.uniform(size=(3,3))
print(z)
print("\nVisualization ")
sb.distplot(random.uniform(size=100),hist=False)
mlt.show()