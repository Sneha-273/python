class parent:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def printinfo(self):
        print(self.name,self.gender)
class child(parent):#accessing parent class
    def __init__(self,name,gender):
        super().__init__(name,gender)
        self.born_year=2003
x=child("sneha","female")
x.printinfo()
print(x.born_year)
