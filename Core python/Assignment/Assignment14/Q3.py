# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
li=['python','java','c','java','python']
s=set(li)
print("List",li)
print("Unique values",s)
for word in s:
    count=li.count(word)
    print(word,'=',count)