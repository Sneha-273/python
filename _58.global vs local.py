a="yes"
def f1():
    print("function 1=",a)
def f2():
    a="hello"
    print("function 2=",a)
def f3():
    global a
    a=1000
    print("function 3=",a)
print("1.")
f1()
print("2.")
f2()
print("3.")
f3()
