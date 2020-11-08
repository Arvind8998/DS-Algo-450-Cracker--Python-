def kedansAlgo(arr):
    currentSum = arr[0]
    overallBestSum = arr[0]
    for i in range(1,5):
        if currentSum >=0:
            currentSum += arr[i]
        else:
            currentSum = arr[i]

        if currentSum > overallBestSum:
            overallBestSum = currentSum
    return overallBestSum

print(kedansAlgo([1,2,3,-2,5]))