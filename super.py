class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
     def __init__(self):
        super().__init__()
        print("Constructor of programmer")
     b=2

class Manager(Programmer):
     def __init__(self):
        super().__init__() # It called the parent class of this class
    # the parent class or super class of Manager is Programmer so first call programmer class then Manager
        print("Constructor of manager")
     c=3

o=Employee()
print(o.a)

a1=Programmer()
print(a1.b,a1.a)

a2=Manager()
print(a2.a,a2.b,a2.c)
