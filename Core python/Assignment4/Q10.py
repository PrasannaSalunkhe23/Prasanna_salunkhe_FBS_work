n=int(input("enter the number:"))

sum=0
for i in range(1,n):
    sum+=i
if sum==n:
    print("perfect number")
else:
    print("not perfect number")