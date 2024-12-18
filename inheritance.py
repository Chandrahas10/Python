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


# Creating objects
a = Employee("Alice", 50000)
b = Programmer("Bob", 70000, "Python")

# Printing company names
print(a.company)  # ITC
print(b.company)  # ITC Infotech

# Displaying details
a.show()  # The name of the Employee is Alice and the salary is 50000
b.show()  # The name of the Employee is Bob and the salary is 70000
b.showLanguage()  # The name is Bob and they are good with Python language
