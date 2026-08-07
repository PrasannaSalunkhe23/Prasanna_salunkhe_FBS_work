# WAP to check if entered number is pallidrome or not.

def pallidrome(num):
    temp = num
    rev = 0
    while (num> 0):
        d = num % 10
        rev = rev  * 10 + d 
        num = num// 10
       # rev = rev  * 10 + d 

    if (rev == temp):
        return True
    else:
        return False

num = int(input("enter the number:"))
res = pallidrome(num)
print(res)