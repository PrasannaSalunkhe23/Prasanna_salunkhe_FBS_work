# 12. Python Program to count number of lowercase characters in a string.
# s=input("Enter string:")
# count=0
# for i in s:
#     if(i.islower()):
#         count=count+1
# print("Number of lowercase letter",count)        

# with method
s=input("Enter the string:")
count=0
for i in s:
    if(i>='a'and i<='z'):
        count=count+1
print("Number of lower case letter",count)        