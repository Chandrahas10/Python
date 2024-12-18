try:
    a =int(input("Hey enter the number  "))
    print(a)

except Exception as e:  #If it false then except condition executed
    print(e)
    

finally:  #It runs if code successuflly run or not it executed
    print("I am inside finally")

def main():
    try:
            a =int(input("Hey enter the number  "))
            print(a)

    except Exception as e:  #If it false then except condition executed
            print(e)


    finally:  #It runs if code successuflly run or not it executed
            print("I am inside finally of function")

main()



