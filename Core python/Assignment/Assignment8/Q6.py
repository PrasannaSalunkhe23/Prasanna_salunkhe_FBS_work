#WAP to print sum of digit of a number.

def sumdigit(num):
    sum = 0
    while (num > 0):
        d = num % 10
        sum = sum +d
        num = num // 10
       
        return sum

num = int(input("enter the number:"))
print('sum of digit =',sumdigit)