#take three digit number
num=int(input("enter a 3 digit number:"))



temp=num
#find digit
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10

#perform operation
reverse=(d1*100) + (d2*10) + d3

# display result
print(f'the reverse of {temp} is{reverse}')