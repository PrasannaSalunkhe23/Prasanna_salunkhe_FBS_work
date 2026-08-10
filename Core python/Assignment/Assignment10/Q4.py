#WAP to reverse the list.

li = [10,20,30,40,40,50]
rev = []
i = len(li)-1
while (i>=0):
    rev.append(li[i])
    i = i-1
print("reverse list =",rev)