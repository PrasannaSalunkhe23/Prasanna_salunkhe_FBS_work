# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

# n=int(input("Enter the n:"))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print('dictionary',d)    

# with method
n=int(input("Enter the n:"))
d={}
for i in range(1,n+1):
    d.update({i:i*i})
print('dictionary',d)    