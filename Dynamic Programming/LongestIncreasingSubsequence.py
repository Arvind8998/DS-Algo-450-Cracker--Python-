def longestInSub(arr):
    dp = [0 for x in range(len(arr)+1)]
    dp[0]=1
    overallMax = 0
    for i in range(0,len(arr)):
        max = 0
        for j in range(0,i):
            if arr[i]>arr[j] :
                if dp[j]> max:
                    max = dp[j]
        dp[i] = max+1
        if(dp[i]>overallMax):
            overallMax = dp[i]
    return overallMax

print(longestInSub([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))