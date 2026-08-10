#WAP to put even and odd elements of a list into two different list.

li = [ 20,35,22,18,99,31]
even =[]
odd=[]
for i in li:
    if( i % 2==0):
        even.append(i)
    else:
        odd.append(i)

print("even list:",even)
print("odd list:",odd)