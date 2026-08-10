#WAP to reverse a given number using recursive function.

def reverseNumber(n , rev):
    if(n > 0):
        d= n % 10
        rev = rev *10 +d
        return reverseNumber(n // 10 ,rev)
    else:
        return rev

n=int(input("enter number:"))
res=reverseNumber(n ,0)
print(res)