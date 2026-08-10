#WAP to remove all occurence of given element.

li = [10,20,10,30,10,40]
n=int(input("enter element to remove:"))

new_list=[]
for i in li:
    if i !=n:
        new_list.append(i)


print("list=",new_list)
