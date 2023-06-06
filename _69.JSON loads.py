#JSON = its text written with javascript object notation
#JSON is syntax for storeing and exchanging data
import json
x='{"name":"kasumi","age":"10","city":"kanto"}'#it must be string
y=json.loads(x)
print(y["age"])