start=int(input("enter start num:"))
end=int(input("enter end num :"))

for i in range(start,end+1):
    if i%7==0 and i%5==0:
        print(i)