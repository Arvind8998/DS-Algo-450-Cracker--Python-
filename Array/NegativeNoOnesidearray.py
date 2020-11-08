# negative no exists from 0 to j-1
# unknown area from i to end

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def rearrange(arr):
    j=0
    for i,value in enumerate(arr,0):
        if(arr[i]<0):
            swap(arr,i,j)
            j=j+1


    return arr

print(rearrange([-12, 11, -13, -5, 6, -7, 5, -3, -6]))