import random
n=random.randint(1,100)
a=-1
guess=0
while (a!=n):
    guess+=1
    a =int(input("Guess the number"))
    if(a>n):
        print("Lower nuber please")
    else:
        print("Higher number please")
    
print(f"You have guess the number correctly in  {guess} attempt")