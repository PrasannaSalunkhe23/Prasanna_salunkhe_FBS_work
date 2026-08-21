# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged
# s1=input("Enter string:")
# new=s1[len(s1)-1]
# for i in range(1,len(s1)-1):
#     new=new + s1[i]
# new=new + s1[0]
# print("Original:",s1)
# print("New string:",new)    

# with method
s=input("Enter the string:")
new=s[len(s)-1]+s[1:len(s)-1]+s[0]
print('New String:',new)
