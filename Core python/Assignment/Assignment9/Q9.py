#WAP to calculate the m to the power n using recursion.

def power(m , n):
    if(n > 0):
        return m * power( m , n-1)
    else:
        return 1

m=int(input("enter the number:"))
n=int(input("enter the value:"))
res=power(m,n)
print(f'raised {m} is power {n} is the {res}')