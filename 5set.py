#Set is a collection of non-repetitive elements.
s={2,5,3,8,5,6,7,5,5,9,0,"HI"} 

e=set() # this is empty set # Don't use s={} 
#Element are not repeated
#unordered & unindexed
#There is no way to change items in sets
print(s,type(s))

s.add(566)
print("add 566 in set :",s,type(s))

s.update([786])
print("update the set ;",s)

s.remove(566)
print("remove the 566 :",s)

n=len(s)
print("length of set :",n)

#Removes the specified element without raising an error if the element is not found.
s.discard(770)
print("remove element if not present not raise error",s)

s.pop()
print("remove the element of set from begining",s)

s.clear()
print("clear the sets",s)

# Returns a new set containing all elements from both sets.
a = {1, 2, 3}
b = {3, 4, 5}
print(a)
print(b)
print("new set containing all element from both a&b",a.union(b))

print("new set with elements common to both sets",a.intersection(b)) #Returns a new set with elements common to both sets.

# Returns a new set with elements in the first set but not in the second.
print("return diiferent set from a & b:",a.difference(b))

# Returns a new set with elements in either set but not in both.
print("new set with elements in either set but not in both.:",a.symmetric_difference(b)) 

# Returns True if the set is a subset of other_set.
print("True if the set is a subset of other_set.",{1, 2}.issubset(a))

# Returns True if the set is a superset of other_set.
print("True if the set is a superset of other_set.:",a.issuperset({1, 2}))

# Returns True if the sets have no elements in common.
print("True if the sets have no elements in common.",a.isdisjoint({6, 7})) 

