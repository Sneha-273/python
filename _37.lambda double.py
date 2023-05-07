def fun(num):
    return lambda a:a*num
one=fun(7)
two=fun(9)
print(one(7))
print(two(9))