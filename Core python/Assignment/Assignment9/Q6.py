#WAP to print fibonacci series using recursive.

def fibonacci(n, a,b):
    if( n > 0):
         c= a + b 
         print('c', end="   ")
         return fibonacci(n -1 , b, c)

n=int(input("enter number:"))
res = (fibonacci n, a,b)
print(res)
