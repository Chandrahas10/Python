# There are many built-in exceptions which are raised in python when something goes 
# wrong.
# Exception in python can be handled using a try statement. The code that handles the 
# exception is written in the except clause.
try:
    a =int(input("Hey enter the number  "))
    print(a)

except ValueError as v:
    print("Invalid data type Enter the integer")
    print(v)

except Exception as e:
    print(e)

print("Thank You")
