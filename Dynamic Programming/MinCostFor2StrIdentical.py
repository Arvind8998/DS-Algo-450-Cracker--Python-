def dpMinCost(X,Y,m,n):
    lcsArr = [[1]*(len(X)+1)] *(len(Y)+1)

    for i in range(len(lcsArr)-1,-1,-1):
        for j in range(len(lcsArr[i])-1,-1,-1):
            # if i== len(lcsArr)-1 and j == len(lcsArr[0])-1:
            #     lcsArr[i][j] = 0
            if i == len(lcsArr)-1 :
                lcsArr[i][j] =0
            elif j == len(lcsArr[i])-1:
                lcsArr[i][j] = 0
            else :
                if(X[i] == Y[j]):
                    lcsArr[i][j] = 1 + lcsArr[i+1][j+1]
                else:
                    lcsArr[i][j] = max(lcsArr[i+1][j], lcsArr[i][j+1])
    print( (len(X)-lcsArr[0][0])*m + (len(Y)-lcsArr[0][0])*n )

X,Y, = "ae#bd","abcd#"
m, n = len(X),len(Y)
# print(m,n)
dpMinCost(X,Y,10,20)