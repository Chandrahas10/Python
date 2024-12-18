# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank you")

# 2. Write a program to print third, fifth and seventh element from a list using enumerate 
# function.

l=[3,4,2,6,8,4,7,4,7]
for i,item in enumerate(l):
    if i==2 or i==4 or i==6 :
     print(item)

# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number

n=int(input("enter the number: "))

table =[n*i for i in range(1,11) ]
print(table)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.

try:
    a=int (input("Enter a:"))
    b=int (input("Enter b:"))
    print(a/b)
except ZeroDivisionError as v:
    print("INfinte")

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n=int(input("enter the number: "))

table =[n*i for i in range(1,11) ]
with open("tables.txt","a") as f:
    f.write(str(table)+"\n")
