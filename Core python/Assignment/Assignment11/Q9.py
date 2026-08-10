numbers = list(range (1,6))

squares=[]
cubes=[]

for i in numbers:
    squares.append(i ** 2)
    cubes.append(i **3)

print("numbers:",numbers)
print("squares:",squares)
print("cubes:",cubes)