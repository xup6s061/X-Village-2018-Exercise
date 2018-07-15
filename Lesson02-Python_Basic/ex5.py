for i in range(2,51):
    flag=True
    for j in range(2,i-1):
        if i%j==0:
            flag=False
    if flag:
        print(i)