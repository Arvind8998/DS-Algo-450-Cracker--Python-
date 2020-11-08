def cycleRotate(arr):
    n =len(arr)
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];

    arr[0] = x;
    return  arr
print(cycleRotate([9, 8, 7, 6, 4, 2, 1, 3]))