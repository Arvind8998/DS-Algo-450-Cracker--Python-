def maximumSum(arr):
    dp = [0 for x in range(0,len(arr)+1)]

    for i in range(0,len(arr)):
        omax = 0
        for j in range(0,i):
            if arr[i]>arr[j] :
                if dp[j]>omax :
                    omax = dp[j]
        dp[i] = omax + arr[i]
    return print(max(dp))

maximumSum([1, 101, 2, 3, 100])