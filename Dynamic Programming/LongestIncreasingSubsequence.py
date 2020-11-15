def longestInSub(arr):
    max = overallMax = 0
    for i in range(0,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] :
                max = arr[j]
        arr[i] = max+1
        if(arr[i]>overallMax):
            overallMax = arr[i]
    return overallMax

print(longestInSub([3, 10, 2, 1, 20]))