# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
s1=input("Enter the string:")
s2=input("Enter the string")
l1=0
l2=0
for i in s1:
    l1=l1+1
for i in s2:
    l2=l2+1
if(l1<l2):
    print("Largest string",s1)
elif(l1>l2):    
    print("Largest string",s2)   
else:
    print("Both string are equal")         