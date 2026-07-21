#WAP TO PRINT GIVEN SERIES IS PRIME OR NOT


startvr=int(input("enter the starting number:"))
endvr=int(input("enter the ending number:"))
print(f'the prime number from {startvr}to{endvr}')

for num in range(startvr,endvr):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)
    else:
        print(f'the number is not prime or composite')

    
