def nextgreaterTemp(temps):
    stack = []
    res = [0] * len(temps)

    for i in range(len(temps)):
        while stack and stack[-1][0] < temps[i]:
            temp, index = stack.pop()
            res[index] = i - index
        stack.append([temps[i], i])

    return res


temps = [71,72,74,70,69,78,71,68]

# res = nextgreaterTemp(temps)
# print(res)




def maxAreaRectangle(rects):
    stack = []


    maxArea = 0
    for i,h in enumerate(rects):
        start = i 
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append([start, h])


    for i,h in stack:
        maxArea = max(maxArea, h * (i - len(rects)))


    return maxArea


rects = [1,2,4,4,5,6,8,2,3]
rects = [1,5,4,4,5,6,8,2,3]
res = maxAreaRectangle(rects)
print(res)
