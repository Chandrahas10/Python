#1. Write a python program to display a user entered name followed by Good
#Afternoon using input () function.

name=input("enter your name:")
print(f"Good Afternoon {name}")

#2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>",name).replace("<|Date|>","30/11/2024")) #this is chaining '.' replace function chaining

#3. Write a program to detect double space in a string
print("double space at index :",name.find("  "))

# 4. Replace the double space from problem 3 with single spaces
print("replace double space with single space :",name.replace("  "," "))
print(name) #name string is not change it make new string is called Immutable string, 
#We cannot change the string

# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"
letter = "\"Dear Harry\" ,\n\tThis python course is nice.\nThanks!"
print(letter)
