class student:
    def __init__(info,name,age,edu):#1.all classes have this function
        info.name=name              #2.execute always ,class being executed
        info.age=age                #3.use=assigning values ,properties
        info.edu=edu
st1=student('ash',10,'Engineer')
print("student name: ",st1.name)
print("student age: ",st1.age)
print('student education: ',st1.edu)