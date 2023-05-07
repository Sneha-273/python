def fun(a):
    return lambda n:n*a
m=fun(5)
print(m(11))
