# 13. Python Program to count number of digits and letters in a string.
# s=input("Enter the string:")
# countNum=0
# countlett=0
# for i in s:
#     if(i.isdigit()):
#         countNum=countNum+1
#     elif(i.isalpha()):
#         countlett=countlett+1
# print("Number of digit:",countNum)
# print("Number of letter:",countlett)

# with methods
s=input("Enter the string:")
countnum=0
countlett=0
for i in s:
    if(i>='0' and i<='9'):
        countnum=countnum+1
    elif(i>='a' and i<='z') or (i>='A' and i<='Z') :
        countlett=countlett+1
print("Number of digits",countnum)
print("Number of letter",countlett)         
