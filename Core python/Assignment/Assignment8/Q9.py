#WAP to check if entered year is leap or not.

def chkleap(year):
    if(year % 400 == 0) or ( year % 4 == 0 and year % 100 != 0):
        print('leap year')

    else:
        print('not a leap year')

year = int(input("enter year:"))
chkleap(year)    