# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String
# s=input("Enter string:")
# n=int(input("Enter the n"))
# new=' '
# for i in range(0,len(s)):
#     if(i!=n):
#         new=new+s[i]
# print("Original String:",s)
# print("New string:",new)        

# with method
str=input("Enter the string:")
n=int(input("Enter the index:"))
new=str[ :n]+str[n+1: ]
print("new String:",new)