import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int (input("enter the value of c:"))

d=b*b-4*a*c

root1=(-b+math.sqrt(d)/(2*a))
root2=(-b-math.sqrt(d)/(2*a))

print("Root1=",root1)
print("Root2=",root2)