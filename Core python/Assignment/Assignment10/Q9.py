#WAP to seprate the even and odd element.

li = [10,15,20,25,30,35]

even =[]
odd = []
for i in li:
    if(i % 2==0):
        even.append(i)
    else:
        odd.append(i)
print("even list=",even)
print("odd list=",odd)