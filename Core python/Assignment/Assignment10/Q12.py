#WAP to print create three list :numbers,squres and cubes

li= [1,2,3,4,5]
numbers =[]
squres = []
cube = []

for i in li:
    numbers.append(i)
    squres.append(i * i)
    cube.append(i * i * i)

print("numbers:",numbers)
print("squres:",squres)
print("cubes:",cube)