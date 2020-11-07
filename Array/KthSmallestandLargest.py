# 0 to j-1  small j++ --> small area increase
# j to i-1 large i++ --> large area increase
# i to r --> unknown area

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr,pivot,l,r):
    i=j=0
    while(i<=r):
        if(arr[i]<=pivot):
            swap(arr,i,j)
            i+=1
            j+=1
        else:
            i += 1
    return j-1

def _quickSelect(arr,l,r,k):
    pivot = arr[r]
    pi = partition(arr,pivot,l,r)
    if k>pi:
       return _quickSelect(arr,pi+1,r,k)
    elif k<pi:
        return _quickSelect(arr,l,pi-1,k)
    else:
        return arr[pi]

arr = [1,3,5,7,8,9,10,13]
print(_quickSelect(arr,0,len(arr)-1,3))