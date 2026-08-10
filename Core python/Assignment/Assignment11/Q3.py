#WAP to sort the 
# list according to the second element in sublist.

li = [[1,5] ,[2,3] , [3,8] ,[4,8]]

li.sort(key = lambda x :x[1])
print(li)