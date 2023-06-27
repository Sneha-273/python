#sub() in regEx used to replace given data with original
import re
x="its holiday time"
y=re.sub("\s","*",x)
print(y)