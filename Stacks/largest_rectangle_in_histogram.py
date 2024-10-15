def largestRectangle(array):
    maxRec = 0
    def inner(arr, index = 0, res = []):
        nonlocal maxRec
        if index == len(arr):
            if res:
                maxRec = max(maxRec, min(res) * len(res))
            return
        res.append(arr[index])
        inner(arr, index + 1, res )
        res.pop()
        inner(arr, index + 1, res )
        return maxRec
    return inner(array)
    ...


def largestRectangle(heights):
    maxArea = 0
    stack = []


    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea




heights = [2,1,5,6,2,3]
res = largestRectangle(heights)
print(res)




def func(rec):

    maxArea = 0

    stack = []


    for i,h in enumerate(rec):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append([start, h])


    for i,h in stack:
        maxArea = max(maxArea, h * (len(rec) - i))


    return maxArea


arr = [1,2,3,4]
res = func(arr)
# res = largestRectangle(arr)
print(res)
