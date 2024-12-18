a=(5,91,3,5,7,"rohan",True)
print(type(a)) #we cannnot change the tuple
#Tuple is Immutable
no=a.count(5) # a count (1) will return number of times 1 occurs in a.
print("number of 5 occuranc :",no)

print(2 in a) # Checks if an element exists in the tuple.

t = (1, 2, 3,67,90,43,5,8)
print("sum:",sum(t)) #print the sum of numeric value in tuple
print("max:",max(t))  # maximum number from tuple
print("min:",min(t))  # minimum number from tuple
print("length",len(t))  #print the length of tuple

i=t.index(90)
print("90 at index foound:",i)

sliced=t[1:4]
print("sliced :",sliced) #slicing of tuple

#unpacking of tuple 
t1=(1,2,3) #in this method tuple elements are initialize in the 
a,b,c=t1   #a,b,c,element 
print(a,b,c)



