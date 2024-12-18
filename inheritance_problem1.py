# # 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# # vector.
class twoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        print(f"the vector is {self.i}i+{self.j}j")

class ThreeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"the vector is {self.i}i+{self.j}j+{self.k}k")
    
a=twoDVector(1,2)
a.show()
b=ThreeDVector(1,2,3)
b.show()

# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow !")
    
d=Dog()
d.bark()

# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary.

class Employee:
    salary = 34000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()
e.salaryAfterIncrement = 40800  # Update salary after increment
print(e.increment)  # Prints the updated increment percentage

# 4. Write a class ‘Complex’ to represent Complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i 

    def __add__(self,c2):
        return Complex(self.r+c2.r,self.i+c2.i)

        
    def __str__(self):
        return f"{self.r}+{self.i}i"

c1 =Complex(1,2)
c2=Complex(3,4)
print(c1 + c2)