#write a program to calculate area of rectangle.

def areaRectangle(l ,b ):
    return  l * b
    
l = int(input("enter the length:"))
b = int(input("enter the breath:"))

res= areaRectangle(l , b)
print(res)