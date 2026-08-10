#WAP to check element present and occurence .

li = [10,20,10,30,10,40]

n=int(input("enter the number:"))
count=0
for i in li:
    if i == n:
        count =count +1

if (count>0):
    print("element is present")
    print("occurence=" ,count)

else:
    print("element is not present")