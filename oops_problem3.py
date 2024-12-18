# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute
class demo:
    a=4
    
o=demo()
print(o.a) #print the class attributes because instance attribute
# is not present
o.a=0  #Insatance attribute is set
print(o.a) #Prints the instance attribute because instance attribute is present
print(demo.a) #Prints the class attribute