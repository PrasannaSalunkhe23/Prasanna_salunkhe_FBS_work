#WAP to find maximum and minimum element of list.

li = [10,48,20,44,6,90]
max =li[0]
min =li[0]

for i in li:
    if (i > max):
        max = i
    if (i <min):
        min = i
print(f"max={max}")
print(f"min={min}")
