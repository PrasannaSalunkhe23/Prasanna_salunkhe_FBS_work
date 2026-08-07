#b)1!+2!+3!+____________+n!

def Sof(n):
    sum=0
    fact=1
    for i in range( 1 , n+1):
        fact *= i
        sum = sum + fact
        return sum
n = int(input("enter the number:"))
res = Sof(n)
print(res)