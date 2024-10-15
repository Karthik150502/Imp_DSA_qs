def rotateArray(arr, n):
    m = n % len(arr)
    for _ in range(m):
        lastEle = arr.pop()
        arr.insert(0, lastEle)
    return arr



arr = [1,2,3,4,5,6,7]
res = rotateArray(arr, 78)
print(res)