# Write  a progrom to find the area and perimeter of following fig (Accept the length,and radius from user)
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth"))
Radius=int(input("Enter the Radius:"))
Area=((length*breadth)+0.5*3.14*Radius**2)
print("Area of figure:",Area)
Perimeter=(2*length)+breadth+3.14*Radius
print("Perimeter of Figure",Perimeter)