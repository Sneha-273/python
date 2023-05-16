class student:
   name=''
   age=0
   def __init__(self,n,a):
        self.name=n
        self.age=a
   def paste(self):
       print(self.name,self.age)
x=student("sai",23)
x.paste()
class person(student):#class:use to don't want add properties or method to class 
    pass