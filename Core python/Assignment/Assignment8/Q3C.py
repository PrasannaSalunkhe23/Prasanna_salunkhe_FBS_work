#1^ 1 +2^2+3^3+4^4+__________+n^N

def Sos(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
    return total

n = int(input("Enter the number: "))
res = Sos(n)
print(res)