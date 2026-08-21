# 2. Python Program to Concatenate Two Dictionaries Into One
# d1={'a':10,'b':20}
# d2={'c':30,'d':40}
# d={}
# for key in d1:
#     d[key]=d1[key]
# for key in d2:
#     d[key]=d2[key]
# print("Dictionary1:",d1)
# print("Dictionary2:",d2)
# print("Concatenate Dictionaries",d)    

# with method:
d1={'a':10,'b':20}
d2={'c':30,'d':40}
print("Dictionary1:",d1)
d1.update(d2)
print("Dictionary2:",d2)
print("Concatenate Dictionaries",d1)