# 4. Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"square is { self.n*self.n}")
    def cube(self):
        print(f"cube is {self.n*self.n*self.n}")
    def sqr_root(self):
        print(f"square root is {self.n**1/2}")

    @staticmethod  #it is used when there is no need of attribute or parameter like self
    def hello():
        print("Hello there !")
    

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.sqr_root()
