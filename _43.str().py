class address:
 def __init__(self,ct,pin):
        self.ct=ct
        self.pin=pin

 def __str__(self):
     f=f'{self.ct} {self.pin}'
     return f
z=address("kolhapur",416202)
print(z)