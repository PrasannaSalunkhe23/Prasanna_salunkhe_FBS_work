# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.
li = [1, 2, 3, 4, 5, 6]
target = int(input("Enter the target sum = "))
pair = set()
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == target:
            pair.add((li[i], li[j]))
print("List =", li)
print("Target =", target)
print("Pair =", pair)