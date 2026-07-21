# take two number
m=int(input("enter the number:"))
n=int(input("enter the number:"))


#display before swapping
print(f'before swapping:m{m}  and n{n}')


#perform operation
m=m+n
n=m-n
m=m-n

#display after number
print(f'after swapping:m{m} and n{n}')

