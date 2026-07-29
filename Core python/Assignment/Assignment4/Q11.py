n=int(input("enter the number:"))

temp=0
sum=0
while temp>0:
    digit=temp%10

    fact=1
    for i in range(1,digit+1):
        fact*=i

    sum+=fact
    temp//=10

    if sum==n:
        print("strong number")
    else:
        print("not perfect number")