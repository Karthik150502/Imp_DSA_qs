def func(arr, timestamp):
    N = len(arr)
    arr.sort()
    l,r = 0, N - 1
    greaterLeast = float("-inf")
    while l<=r:
        mid = l + (r - l)//2
        if arr[mid] < timestamp:
            greaterLeast = max(greaterLeast,arr[mid])
            l = mid + 1
        else:
            r = mid - 1
    return greaterLeast if greaterLeast != float("-inf") else -1     


def func2(values, timeStamp):
    values
    N = len(values)
    l,r = 0, N - 1
    res = timeStamp
    while l<=r:
        mid = l + (r - l)//2

        if values[mid] <= timeStamp:
            res = values[mid]
            l = mid + 1
        else:
            r = mid - 1
    return res

arr = [1,2,4,6,7,9,11,12]
arr = [-4,-3,-1,0,1,2,5,6,8,9,10,11,12]

res = func2(arr, 8)
print(res)