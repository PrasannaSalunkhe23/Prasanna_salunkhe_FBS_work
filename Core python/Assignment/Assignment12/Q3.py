# 3. Python Program to Detect if Two Strings are Anagrams
# s1=input("Enter the string:")
# s2=input("Enter the string:")
# counts1=0
# counts2=0
# if(len(s1)!=len(s2)):
#     print("Npt Anagram")
# else:
#     for ch in s1:
#         for i in s1:
#             if(ch==i):
#                 counts1+=1
#         for j in s2:
#             if(ch==j):
#                 counts2+=1
#     if(counts1==counts2):
#         print("Anagram")
#     else:
#         print("Not Anagram")     

# with method
s1=input("Enter the String:")
s2=input("Enter the string")
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")    
