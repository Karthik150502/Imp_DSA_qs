def func(arr):


    maxArea = 0

    stack = []

    for i, h in enumerate(arr):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index)) 
            start = index
        stack.append([start, h])


    

    for i,h in stack:
        maxArea = max(maxArea, h * (len(arr) - i))

    return maxArea



arr = [1,4,5,6,3,2,5,3,2,6]
res = func(arr)
print(res)