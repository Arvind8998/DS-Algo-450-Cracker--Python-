def minimiseHeight(arr,n,k):
    arr.sort()
    small = arr[0]+k
    big = arr[n-1]-k
    ans = arr[n-1]-arr[0]
    if small>big:
        small,big = big,small

    for i in range(1,n-1):
            subtract = arr[i]-k
            add = arr[i] + k

            if subtract >= small or add <= big:
                continue

# either current element would be biggest(add-small) or least(big-subtract) greedy approach

            if big-subtract  <= add-small:
                small =subtract
            else:
                big = add

    return  min(ans,big-small)

print(minimiseHeight([1, 5, 15, 10],4,3))






