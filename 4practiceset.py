#1. Write a program to store seven fruits in a list entered by the user

print("problem 1")
fruit=[]
n=int(input("define the length of list: \t"))
for i in range(0,n):
    f1=input(f"enter the fruit name {i+1}:\t")
    fruit.append(f1)
print(fruit)

#2. Write a program to accept marks of 6 students and display them in a sorted manner
print("problem 2")
mark=[]
n=int(input("Number of student: \t"))

for i in range(0,n):
    m1=int (input(f"Enter the mark of first student {i+1}:\t"))
    mark.append(m1)
print(mark)
mark.sort()
print("After sorting",mark)

# #3change tuple into list
print("problem 3")
mark=(45,67,43,67)
print(type(mark))
l=list(mark)
print(type(l))
print(l)

#4. Check that a tuple type cannot be changed in python.
# a=(34,56,45)
# a[2]=90  #It cannot be changed bcoz it is immutable

#4. Write a program to sum a list with 4 numbers.
print("problem 4")
n1=[]
for i in range(0,4):
    m1=int (input(f"Enter the number {i+1}:\t"))
    n1.append(m1)
print(n1)
print("sum of numbers",sum(n1))

# 5. Write a program to count the number of zeros in the following tuple:
print("problem 5")
a = (7, 0, 8, 0, 0, 9)
b=a.count(0)
print("occurance of 0",b)
