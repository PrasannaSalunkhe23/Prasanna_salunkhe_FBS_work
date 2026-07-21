# take input basic salary
basic=float(input("enter basic salary:"))

da=basic*10/100
ta=basic*12/100
hra=basic*15/100

total_salary=basic+da+ta+hra


print(f'total salary of employee is {total_salary}')