#WAP to find fictorial using recursive.

def factorial(n):
    if (n > 0 ):
        return 0 * factorial (n-1) 
    else:
        return 1

n=int(input("enter number:"))
res = factorial(n)
print(res)