# take three digit number
num=int(input("enter the three digit number:"))

# store original num so take variable
temp=num

# find digit
d1=num % 10
num= num//10
d2=num%10
num=num//10
d3=num%10
num=num//10

#calculate sum of digit
sum_digit=d1+d2+d3

print(f'the sum of {temp} is {sum_digit}')