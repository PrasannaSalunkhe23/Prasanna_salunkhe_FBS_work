# WAP to print reverse of following number.

def reverse(num):
    temp = num
    rev = 0
    while (num > 0):
        d = num%10
        num = num // 10
        rev = rev * 10 + d

    return rev    
num = int(input("enter the number:"))
res = reverse(num)
print(res)