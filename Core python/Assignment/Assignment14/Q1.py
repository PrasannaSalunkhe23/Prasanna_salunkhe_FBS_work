# 1. Write a Python program to find elements in a given set that are not in
# another set.
S1={10,20,30,40}
S2={20,60,80,100}
print("set1:",S1)
print("set2:",S2)
res=S1.difference(S2)
print("Elements in set 1 but not in S2",res)
