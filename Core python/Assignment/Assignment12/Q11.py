# 11. Python Program to replace every blank space with hyphen in a string.
s=input("Enter the string:")
new=''
for i in s:
    if i==' ':
        new=new+'-'
    else:
        new=new+i
print("original string:",s)
print("New string:",new)
