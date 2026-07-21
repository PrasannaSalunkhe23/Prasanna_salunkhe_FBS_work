days=int(input('enter a days:' ))

year = days // 365
#print(year)

days=days%365
#print(day)

week=days//7
#print(week)

days=days%7
#print(days)

print(f'Year:{year},Week:{week},days:{days}')