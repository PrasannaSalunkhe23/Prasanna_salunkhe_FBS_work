# 7. Python Program to Remove the Given Key from a Dictionary
d={'id':101,'name':'harshada','age':20}
key=input("Enter key to search:")
if key in d:
    d.pop(key)
    print("Updated Dictionary=",d)
else:
    print("Key does not exist")    