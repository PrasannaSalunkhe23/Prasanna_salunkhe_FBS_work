#WAP to list after removing even number.

li =[10,15,20,25,30,35]

new_list = []

for i in li:
    if( i % 2 != 0):
        new_list.append(i)
print("list after removing number=",new_list)