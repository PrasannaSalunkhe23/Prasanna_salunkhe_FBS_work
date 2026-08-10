#wap to find of sum of following series using recursive function.

def fact(n):
    if(n>0):
        return n* fact(n-1)
    else:
        return 1


def sumFact(n):
    if(n>0):
        return fact(n) + sumFact(n-1)
    else:
        return 0

n=int(input('enter number:'))
res=sumFact(n)
print(f'sum of fact:',res)