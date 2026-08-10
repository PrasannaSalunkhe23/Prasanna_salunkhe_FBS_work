#WAP to create a duplicate of an existing list it should not print to same list.

li = [10,20,30,40,50]

new_list=[]
for i in li:
    new_list.append(i)

print("original list=",li)
print("duplicate list=",new_list)