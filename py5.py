def func(arr, k):
    result = []
    def recur(arr, index = 0, res = []):
        if k == len(res):
            result.append(res.copy())
            return
        
        for i in range(index, len(arr)):
            res.append(arr[i])
            recur(arr, i + 1, res)
            res.pop()
    recur(arr)
    return result


# arr = [1,2,3,4,5,6]
# k = 2

# res = func(arr, 5)

# print(res)




def func2(arr, k):



    res = []
    for i in range(len(arr) - (k - 1)):
        res.append(arr[i:i + k])


    return res


arr = [1,2,3,4,5,6]
k = 3
res = func2(arr, k)
print(res)
