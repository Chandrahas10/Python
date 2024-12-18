# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up
print("Problem 1")
words ={
    "help":"madat",
    "cat":"billi",
    "woman":"stree",
    "chair":"kursi"
}
word=input("Enter the word :")
print(words[word])

print("Problem 2")
#2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).
s = set()
for i in range(0,8):
  n=int(input("Enter number "))
  s.add(int(n))
print((s))

print("Problem 3")
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s=set()
s.add(18)
s.add("18")
print(s)

# 4. What will be the length of following set s:
print("Problem 4")
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s)) #length is 2
#20==20.0 is true Python compares the values, 
# and 20 (an integer) is equal to 20.0 (a floating-point number)

# 5. s = {}
# What is the type of 's'?
print("Problem 5")
s={}
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.
print("Problem 6")
d={}
for i in range(0,4):
  name=input("Enter name :")
  lan=input("Enter language :")
  d.update({name:lan})
print(d.items())

# 7.If the names of 2 friends are same; what will happen to the program in problem 6
print("Problem 7")
d={}
for i in range(0,4):
  name=input("Enter name :")
  lan=input("Enter language :")
  d.update({name:lan}) #If the key are same key is update
print(d.items())  #if value is same it is not problem

# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
 #-> we cannot include list in set 
 #->    we cannot change with indexing values
 #-> No, you cannot include a list in a set in Python. 
 #->This is because sets require all their elements to be immutable
 #-> (unchangeable) and hashable, and lists are mutable, so they cannot be part of a set.