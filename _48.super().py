#super()=access to all properties and methods from parent class
class parent:
    n=''
    l=0
    def __init__(self,name,lname):
        self.n=name
        self.l=lname
    def info(self):
        print(self.n,self.l)
class child(parent) :
    def __init__(self,name,lname):
        super().__init__(name,lname)
z=child("rudra",100)
z.info()