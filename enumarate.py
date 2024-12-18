l=[3,4,6,8,4,64]

index =0
for item in l:
    print(f"The item number is {index} is {item}")
    index+=1

#This can be simplified by usnig enumarate function


for index, item in enumerate(l):
    print(f"The item number {index} is {item}")