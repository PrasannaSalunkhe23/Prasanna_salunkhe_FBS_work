#WAP to find sum od n number using recursive.

def soN(n):
    if ( n > 0):
        return n + soN(n-1)
    else:
        return 0
n=int(input("enter number:"))
res=soN(n)
print(res)