try:
    a =int(input("Hey enter the number  "))
    print(a)

except Exception as e:  #If it false then except condition executed
    print(e)
    

else:  #If it successfully run then else condition executed
    print("I am inside else")
