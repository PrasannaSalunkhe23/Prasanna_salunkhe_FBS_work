# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

# d={'id':101,'name':'harshada','age':20}
# key=input("Enter key to search:")
# if(d.get(key)!=None):
#     print("Key exists in Dictionary")
# else:
#     print("Key does not exist in Dictionary")   

# with method
d={'id':101,'name':'harshada','age':20}
key=input("Enter key to search:")
if(key in d):
    print("key exist in Dictionary")
else:
    print("Key does not exist in Dictionary") 
