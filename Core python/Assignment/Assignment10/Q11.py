#WAP to print number divisible by m and n

li =[10,15,20,30,40,50,60]

m=int(input("enter m:"))
n=int(input("enter n:"))

for i in li:
    if ( i %m==0 and i%n==0):
        print(i)
