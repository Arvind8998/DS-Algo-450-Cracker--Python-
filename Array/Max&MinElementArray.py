def maxmingetter(inputarr):
    n = len(inputarr)
    maxele = minele = 0
    if n%2 == 0:
            maxele = max(inputarr[0],inputarr[1])
            minele = min(inputarr[0],inputarr[1])
            i = 2
    else :
        maxele = minele = inputarr[0]
        i=1

    while(i<n-1):

        if inputarr[i] > inputarr[i+1]:
            # next element is smaller
            maxele = max(maxele,inputarr[i])
            minele = min(minele,inputarr[i+1])
        else :
            # next element is larger
            maxele = max(maxele,inputarr[i+1])
            minele = min(minele,inputarr[i])

           # two element compared in single iteraion
        i+=2
    return[maxele,minele]


print(maxmingetter([12, 32, 45, 67, 89, 10, 5]))
