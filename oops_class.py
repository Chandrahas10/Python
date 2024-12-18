class Employee:
    name = "harry"  # Class attribute
    language = "python"
    age = 18
    salary = 50000  
    
    def __init__(self,name,salary,language): #dunder method which is automatically call
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    
    def getinfo(self):
        print(f"My name is {self.name} the language is {self.language}.The salary is {self.salary}")
# rohan = Employee()
harry = Employee("Haarry",16000,"javascript")
# print(rohan.name,rohan.language, rohan.age)
# rohan.getinfo()
harry.getinfo()
