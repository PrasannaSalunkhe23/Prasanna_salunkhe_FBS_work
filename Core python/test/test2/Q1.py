# Q1.write a program to print find prime number
n=int(input("Enter the number:"))
count=0
num=2
print(f'First {n} Prime number')
while count<n:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        count=count+1
    num=num+1    

        