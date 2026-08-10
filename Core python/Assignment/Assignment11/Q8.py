for i in range(10 , 0 , -1):
    start=(i - 1) * 10 +1
    end = i * 10

    if i % 2 ==0:
        for j in range(start , end+1):
            print(j , end = "\t ")

    else:
        for j in range(end , start -1 , -1):
            print(j, end="\t")
    print()