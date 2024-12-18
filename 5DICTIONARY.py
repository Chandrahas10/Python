# Dictionary is a collection of keys-value pairs
# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys

d={} #empty dictionary
mark ={
    "Chandu":100,
    "swapnil":90,   #syntax of dictionary
    "tejas":99,
    0:"harry"
}
print(mark,"\n",type(mark))
print("value assign to Chandu",mark["Chandu"])

print("Items of mark",mark.items())
print("key",mark.keys())  #print the keys of dictionary
print("Value",mark.values())  #print the values of dictionary

mark.update({"swapnil":98, "Rohan":77})
# Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
print("upadate Swapnil & Rohan :",mark)

#Returns the value for the specified key. If the key is not found, returns the default value.
print(mark.get("Chandu"))
print(mark.get("chandu")) #It print none
print(mark["Chandu"])  #if key is not present it shows the error
# the output of print(mark.get("Chandu")) &print(mark.get("chandu")) is same

print(mark.pop("Chandu")) #delete the key 
print(mark)
print(mark.popitem())   #delete the last item
print(mark)
mark.clear()
print(mark)  

copy1=mark.copy() #It copy mark into copy1 mark is none
print(copy1)
