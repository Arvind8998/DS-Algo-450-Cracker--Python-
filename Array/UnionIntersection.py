def printUnion(arr1,arr2,n1,n2):
    hs = set()

    for i,value in enumerate(arr1):
        hs.add(arr1[i])
    for j,value in enumerate(arr2):
        if not arr2[j] in hs:
            hs.add(arr2[j])

    for i in hs:
        print(i)

def printIntersection(arr1,arr2,n1,n2):
    hs = set()
    intersection = []
    for i, value in enumerate(arr1):
        hs.add(arr1[i])
    for j, value in enumerate(arr2):
        if arr2[j] in hs:
            intersection.append(arr2[j])

    for i in intersection:
        print(i)


arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)

# Function call
printUnion(arr1, arr2, n1, n2)
printIntersection(arr1, arr2, n1, n2)