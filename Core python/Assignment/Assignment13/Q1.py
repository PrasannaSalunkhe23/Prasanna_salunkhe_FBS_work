# 1. Python Program to Add a Key-Value Pair to the Dictionary
# d={'id':101,'name':'harshada','age':20}
# key=input("Enter the key:")
# value=input("Enter the value:")
# d[key]=value
# print("Update the dictionary",d)

# with method
d={'id':101,'name':'harshada','age':20}
key=input("Enter the key:")
value=input("Enter the value:")
d.update({key:value})
print("Update the dictionary",d)
