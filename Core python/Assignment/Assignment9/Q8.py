#WAP to check wheather a number is prime or not using recursion .

def prime(num ,i):
    if(num == i):
        return True 
    if(num % i == 0):
        return False
    return prime (num , i+1)
num=int(input("enter number:"))
if(num > 1):
    res= prime (num , 2)
    if(res):
        print("number is prime") 

    else:
        print("number is not prime")

else:
    print("number is not pirme")
