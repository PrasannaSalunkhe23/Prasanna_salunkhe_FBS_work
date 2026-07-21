days=int(input("Enter the days:"))

year=days//365
print(year)

days=days%365
print(days)

week=days//7
print(week)

days=days%7
print(days)

print(f'year:{year},week:{week},days:{days}')