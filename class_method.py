class Employee:
    a=1
    @classmethod  #It is used to show the class attribute not instant attribute like 45
    def show(cls):
        print(f"The class value of a is {cls.a}")

e=Employee()
e.a=45
e.show() 