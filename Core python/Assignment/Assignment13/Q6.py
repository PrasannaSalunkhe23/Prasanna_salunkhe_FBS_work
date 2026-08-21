# 6. Python Program to Multiply All the Items in a Dictionary
# d={'a':10,'b':20,'c':30,'d':20,}
# mul=1
# for i in d:
#     mul=mul*d[i]
# print("multiply of all items:",mul)    

# with method
d={'a':10,'b':20,'c':30,'d':20,}
mul=1
for i in d.values():
    mul=mul*i
print("multiply of all items:",mul)    