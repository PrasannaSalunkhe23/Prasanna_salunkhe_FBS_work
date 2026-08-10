#WAP to check if given number is Armstrong or not using recursive function.

def armStrong(n):
    if (n>0):
        d=n % 10
        return d** count +armStrong(n//10)
    else:
        return 0

n=int(input('enter number:'))
count=len(str(n))
res=armStrong(n)
if (res==n):
    print("armstrong number")
else:
    print("not armstrong number")    