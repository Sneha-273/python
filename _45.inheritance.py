class person:
 def __init__(self,ft,lt):
        self.ft=ft
        self.lt=lt
 def __str__(self):
     return  f"{self.ft} {self.lt}"
p=person("misty","villamn")
print(p)