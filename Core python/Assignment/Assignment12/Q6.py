# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen
s=input("Enter the string:")
new=' '
for i in s:
    if(i==' '):
        new=new+'-'
    else:
        new=new+i
print("Original string:",s)
print("New string:",new)
