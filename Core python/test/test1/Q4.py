# Calculate the cost of painting the following  building's walls (both interior and exterior)you  need to accept area (one wall)and cost of both interior and exterior wall
Area=int(input("Enter the Area of wall:"))
exterior=int(input("Enter the Exterior Wall:"))
interior=int(input("Enter the Interior Wall:"))


exterior_cost=exterior*Area
interior_cost=interior*Area
total=interior_cost + exterior_cost

print('Cost of paintaing is',total)


