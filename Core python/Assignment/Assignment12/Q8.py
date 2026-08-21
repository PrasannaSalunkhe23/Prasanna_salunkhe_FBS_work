# 8. Python Program to Remove the Characters of Odd Index Values in a
# String
s=input("Enter the string:")
new=' '
for i in range(0,len(s)):
    if(i%2==0):
        new=new+s[i]
print("Original list:",s)
print("String list:",new)
