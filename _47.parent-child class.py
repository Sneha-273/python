class parent:#being inherited from  (gives services)
    def __init__(self,name,s_name):
        self.name=name
        self.s_name=s_name
    def info(self):
        print(self.name,self.s_name)
class child(parent):#take sevices
    def __init__(self,name,s_name):
        parent.__init__(self,name,s_name)#parent init() call to keep parent's inheritance
x=child("janaki","daas")
x.info()


