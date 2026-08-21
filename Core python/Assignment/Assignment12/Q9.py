# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
# s=input('Enter String:')
# countch=0
# countw=1
# for i in s:
#     if(i!=' '):
#         countch=countch+1
#     if(i==' '):
#         countw=countw+1
# print("Number of character:",countch)
# print("Number of words",countw)           

# with method
s=input("Enter the string:")
word=s.split()
characters=len(s.replace(' ',''))
print("Number of word:",len(word))
print("Number of character",characters)