#function definition
def sum():

   a=int(input("Enter the number"))
   b=int(input("Enter the number"))
   c=int(input("Enter the number"))
   average=(a+b+c)/3
   print(average)

sum() #function call

# function with parameter
def quick(name):
    print("Good morning "+name)

quick("chandu")