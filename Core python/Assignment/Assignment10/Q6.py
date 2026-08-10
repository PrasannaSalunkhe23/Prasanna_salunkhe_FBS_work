#WAP  to print remove duplicates.

li =[10,20,10,30,20,40]
new_list =[]

for i in li:
    found = False
    for j in new_list:
        if i ==j:
            found =True
            break
    if found == False:
            new_list.append(i)
print("list after removing duplicates =",new_list)