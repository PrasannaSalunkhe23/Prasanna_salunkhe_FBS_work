n = int(input("enter number of coins:"))
coins=list(map(int,input("enter coins:").split()))
for i in coins:
    if coins.count(i)%2!=0:
        print("Missing coin:",i)
        break