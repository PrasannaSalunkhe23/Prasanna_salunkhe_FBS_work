num=int(input("enter a 3 digit number:"))

rev=(num%10) * 100 + ((num//10) %10 ) *10 + (num//100)


if num == rev:
    print("palidrome")
else:
    print("not palidrome")