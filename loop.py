n=int (input("Enter a number "))
for i in range (n):
    print(i)
    

i = 0
while i < 5: # print "Harry" – 5 times!
 print("Harry") 
 i = i + 1

l = [1, 7, 8]
for item in l: #
    print("print items of list",item) # prints 1, 7 and 8 

# range(start, stop, step_size)
# step_size is usually not used with range()

l= [1,7,8]
for item in l:
 print(item)
else:
 print("done") # this is printed when the loop exhausts!


#Break
#‘break’ is used to come out of the loop when encountered. It instructs the program to –
# exit the loop now

for i in range (n):
    if(i==2):
     break
    print("If condition is satisfied i==2 it will break",i)

#continue
#‘continue’ is used to stop the current iteration of the loop and continue with the next 
# one. It instructs the Program to “skip this iteration”.

for i in range (n):
    if(i==2): # if i is 2, the iteration is skipped 
     continue
    print("If condition is satisfied i==2 it will continue",i)

#pass
# pass is a null statement in python.
# It instructs to “do nothing”.

for i in range (n):
    if(i==2): # if i is 2, the iteration is skipped 
     continue
    print("If condition is satisfied i==2 it will pass",i)
