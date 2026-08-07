#WAP to find sum of following series using function.
#1+2+3+4+5+____+n

def Sos(n):
    if(n > 0):
         return n + Sos (n-1)
    else:
         return 0

n= int (input("enter the number:"))
res=Sos(n)
print(res)