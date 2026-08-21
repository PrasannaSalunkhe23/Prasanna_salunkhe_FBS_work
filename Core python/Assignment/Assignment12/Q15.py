# 15. Python Program to find larger string without using built-in functions.
# s1=input("Enter the string:")
# s2=input("Enter the string")
# l1=0
# l2=0
# for i in s1:
#     l1=l1+1
# for i in s2:
#     l2=l2+1
# if(l1<l2):
#     print("Largest string",s1)
# elif(l1>l2):    
#     print("Largest string",s2)   
# else:
#     print("Both string are equal")         

# with method:
n=int(input("Enter the number of string:"))
large=''
for i in range(n):
    s=input("Enter string:")
    count=0
    for i in s:
        count=count+1
        large_count=0
    for j in large:
        large_count=large_count+1
    if count > large_count:
        large=s
print("Larger string:",large)        
