def topKElements(nums, k):
    record = [[] for _ in range(len(nums) + 1)]
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)

    for key, value in counter.items():
        record[value].append(key)
    result = []
    for i in range(len(record) - 1, -1, -1):
        if len(result) == k:
            break        
        if record[i] == []:
            continue
        else:
            result.extend(record[i])
    return result


arr =[1,1,1,2,2,3,4,4,4,4,5,5,5,5]
k = 3
print(topKElements(arr, k))
        