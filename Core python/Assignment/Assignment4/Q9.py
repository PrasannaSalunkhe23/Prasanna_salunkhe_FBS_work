start=int(input("enter start number:"))
end=int(input("enter end number:"))
num=int(input("enter the divisor" ))


for i in range(start,end+1):
    if i%num==0:
        print(i)