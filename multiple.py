class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and they are good with {self.language} language")


class Coder(Employee):
    company = "Microsoft"

    def __init__(self, name, salary, course):
        super().__init__(name, salary)  # Only pass `name` and `salary` here
        self.course = course

    def courses(self):
        print(f"The name is {self.name} and they learn {self.course} course")


# Creating objects
a = Employee("Alice", 50000)
b = Programmer("Bob", 70000, "Python")
c = Coder("Chandu", 60000, "DSA")

# Printing company names
print(a.company)  # ITC
print(b.company)  # ITC Infotech
print(c.company)  # Microsoft

# Displaying details
a.show()  # The name of the Employee is Alice and the salary is 50000
b.show()  # The name of the Employee is Bob and the salary is 70000
b.showLanguage()  # The name is Bob and they are good with Python language
c.courses()  # The name is Chandu and they learn DSA course
