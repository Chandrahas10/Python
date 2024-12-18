def myFun():
    print(" Hellow World")

if __name__=="__main__":
    #if this code is executed by running the file its present in
    print("we are directly running this code")
    myFun()
    print(__name__) #if you run this in their original file then it display __main__

# if it run this file in imported file it display original file name