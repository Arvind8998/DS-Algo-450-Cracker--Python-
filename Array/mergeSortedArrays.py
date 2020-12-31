def _mergeSortedArray(arr1,arr2):
    m, n, i, j, k = len(arr1), len(arr2), 0, 0, 0
    resLen = m + n
    resultarray = [0 for i in range(resLen)]

    while i< m and j < n:
        if arr1[i] < arr2[j]:
            resultarray[k] = arr1[i]
            i += 1
            k += 1
        else :
            resultarray[k] = arr2[j]
            j += 1
            k += 1

    while i< m:
        resultarray[k] = arr1[i]
        i +=1
        k +=1

    while j< n:
        resultarray[k] = arr2[j]
        j +=1
        k +=1

        
    return resultarray

print(_mergeSortedArray([1, 2, 3,4],[2,4,6]))

