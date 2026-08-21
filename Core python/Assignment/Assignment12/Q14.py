# 14. Python Program to count the occurrences of ach word in a string.
s=input("Enter String:")
word=s.split()
for i in range(len(word)):
    count=0
    if(word[i] not in word[ :i]):
        for j in word:
            if(word[i]==j):
                count=count+1
        print(word[i],'=',count)