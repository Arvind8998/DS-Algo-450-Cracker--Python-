def sorter(arr):
    count0 = count1 = count2 = 0
    for index,val in enumerate(arr):
        if val == 0:
            count0+=1
        elif val == 1:
            count1+=1
        else:
            count2+=1

    print("zero",count0,"one",count1,"two",count2)
    arrindex = 0
    
    while count0 >0:
        arr[arrindex] = 0
        arrindex+=1
        count0 -=1
    while count1 >0:
        arr[arrindex] = 1
        arrindex+=1
        count1 -= 1
    while count2 >0:
        arr[arrindex] = 2
        arrindex+=1
        count2 -= 1

    return arr

print(sorter([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]))
