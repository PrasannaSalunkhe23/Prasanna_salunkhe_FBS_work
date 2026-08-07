def chkArmstrong(num):
    temp=num
    count=len(str(num))
    sum=0
    while(num> 0):
        d = num % 10
        sum = sum +(d ** count)
        num = num //10

        if( temp == sum):
            print(f'{temp} is Armstrong number.')

        else:
            print(f'{temp} is not armstrong number')

num=int(input('enter the number:'))
chkArmstrong(num)