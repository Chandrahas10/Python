#Python lists are containers to store a set of values of any data type.
friend=["Apple","Orange","Akash",3,890,False]
print(type(friend))
print(friend[1])
friend[1]="Grapes" #this shows we can change the list 
print(friend[1])   #list are Mutable

print(friend[1:5])

friend.append("chandu")
print(friend)

num=[2,56,4,78,90,34 ]
num.sort()  #sort the list 
print(num)
num.reverse()  #reverse the list 
print(num)
num.insert(0,33333) #insert 33333 such that its index in the list is 0
print(num)
print(num.pop(0))  #delete the given index 0 element from list
print(num)
num.remove(78)   #remove the 78 element
print(num)