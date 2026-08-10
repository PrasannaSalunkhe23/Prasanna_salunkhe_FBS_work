#WAP to find the second largest number using bubble sort.

li = [10,40,20,50,30]

n = len(li)
for i in range(n):
    for j in range(0 , n -i -1):
        if li[j] >li[j+1]:
            li[j] ,li[j+1] =li[j+1],li[j]


print("sorted list:",li)
print("second largest :",li[-2])