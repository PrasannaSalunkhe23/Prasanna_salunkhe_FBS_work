#WAP to find sum of digit using recursive.

def soD(n):
    if(n>0):
        d= n % 10
        n = n//10
        return d +soD(n)
    else:
        return 0

n=int(input("enter the number:"))
res=soD(n)
print(res)