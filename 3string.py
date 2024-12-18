#string
a='chandu' #single quoted string
b="kori" #double quoted string
c='''chandu ''' #triple quoted string select multiple line twinkle twinkle little star
print("print a string :",a)
print("print type of a string :",type(a))
# it is immutable it cannot be change string element

#slicing string 
name="chandu"
print("slicing the string:",name[0:3])

# negative slicing
print("negative slicing :",name[-4:-1]) 
# "c  h  a  n  d  u"
# -6,-5,-4,-3,-2,-1 like that indexing in negative slicing
#  0, 1, 2, 3, 4, 5 in positive slicing 
print("positive :",name[2:5])
print(name[:5]) #is same as print(name[0:4])
print(name[2:]) #is same as print(name[2:5])
print("another tenchnique for slicing :",name[1:4:3])
  #"chandu" start from index 1 stop before index 4,jump by 3 index

print("print length string:",len(name))#string length
print(name.endswith("ndu")) #name string is end with "ndu"
print(name.startswith("cha")) #name string is start with "cha"
print(name.capitalize()) #capitalize the first letter

# add the another string at the middle of string 

nameshort=name[:len(name)//2]+a+name[len(name)//2:]
print("after the adding the string at the middle of another string:",nameshort)

