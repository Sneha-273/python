import matplotlib.pyplot as mlt
import seaborn as sb
from numpy import  random
sb.distplot(random.normal(loc=5,scale=10,size=100),hist=False,label="normal")
sb.distplot(random.binomial(n=5,p=0.5,size=100),hist=False,label="binomial")
mlt.show()