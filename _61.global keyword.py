#global =use it to make variable global
def fun():
    global z
    z="it becomes global"
fun()
print(z)