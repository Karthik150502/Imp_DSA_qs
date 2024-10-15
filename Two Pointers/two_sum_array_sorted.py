def twoSumInSortedArray(arr, target):
    i,j = 0, len(arr) - 1
    while i < j:
        if (arr[i] + arr[j]) < target:
            i += 1
        elif (arr[i] + arr[j]) > target: 
            j -= 1
        else: 
            return i+1,j+1
    return []

arr = [1,2,3,4,5,6]
target = 8

print(twoSumInSortedArray(arr, target))

