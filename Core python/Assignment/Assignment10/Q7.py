#WAP to create a new list from existing list which contain cube of each number  of ;ist.

li = [1,2,3,4,5]

cube= []
for i in li:
    cube.append(i * i * i)
print("original list=",li)
print("cube list=",cube)