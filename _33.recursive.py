def fact(num):
    if num==1:
         return 1
    else:
         return (num*fact(num-1))
a=int(input('enter number='))
print("factorial of ",a,"is",fact(a))