#5.write a python program to find the longest comman prefix of string. Use the python etc.

li = ['flow','flower','flight']
s1 =set()
s2 =set()
s3 =set()

for i in range(1 ,len(li[0]) + 1):
    s1.add(li[0][:i])
for i in range(1, len(li[1]) + 1):
    s2.add(li[1][:i])
for i in range(1, len(li[2]) + 1):
    comman = s1.intersection(s2,s3)
    longest = ' '
for word in comman:
    if len(word) > len(longest):
        longest = word
print("String =" ,li)
print("Longest common prefix =" , longest)