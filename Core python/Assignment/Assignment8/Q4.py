#WAP sum of all odd number between 1 to n

def Odd_num(n):
    total = 0
    for i in range(1, n + 1, 2):
        total = total + i
    return total

n = int(input("Enter the number: "))
res = Odd_num(n)
print(res)