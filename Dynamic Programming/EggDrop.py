import sys

def mindroptoCriticalFloor(e,f):
    dp = [[0 for x in range(f+1)] for x in range(e+1)]
    for i in range(1,e+1):
        for j in range(1,f+1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = 1
            else:
                minval = sys.maxsize
                prj = 0
                for myj in range(j-1,-1,-1):
                    v1 = dp[i][myj]
                    v2 = dp[i-1][prj]
                    prj += 1
                    maxval = max(v1,v2)
                    minval = min(maxval,minval)
                dp[i][j] = minval+1
    print(dp)
    return  dp[e][f]

print(mindroptoCriticalFloor(2,36))