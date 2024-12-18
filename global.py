a=89 # it is global variable
print(a)

def fun():
    global a
    print(a)
    a=3 # it is local variable
    print(a)


fun()