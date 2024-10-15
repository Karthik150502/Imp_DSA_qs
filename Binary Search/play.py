def func(arr):
    stack = []
    maxArea = arr[0]


    for i,h in enumerate(arr):
        start = i

        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append([start, h])



    for i,h in stack:
        maxArea = max(maxArea, h *( len(arr) - i)) 

    return maxArea

heights = [4,5,8,6,3,9,3,6,1,8,4,1,6]
res = func(heights)
print(res)



def func2(temps):

    res = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and stack[-1][1] < t:
            index, temp = stack.pop()
            res[index] = i - index
        stack.append([i, t])


    return res


temps = [70,71,72,70,69,68,78,71,69]
# [1, 1, 4, 3, 2, 1, 0, 0, 0]
res = func2(temps)
print(res)


def func3(position, speeds, target):

    posAndSpeeds = [[p,s] for p,s in zip(position, speeds)]
    posAndSpeeds.sort(key = lambda x:x[0], reverse=True)
    hours = []

    for p,s in posAndSpeeds:
        timeToReach = (target - p) / s
        hours.append(timeToReach)
        if len(hours) > 1 and hours[-1] <= hours[-2]:
            hours.pop()


    return len(hours)


positions = [10,8,0,5,3]
speeds = [2,4,1,1,3]

target = 12

res = func3(positions, speeds, target)

print(res)





def func4(nums):



    N = len(nums)
    res = [-1] * N 

    stack = []
    for i in range(N * 2):
        ind = i % N
        while stack and stack[-1][0] < nums[ind]:
            smallerNum, index = stack.pop()
            res[index] = nums[ind]

        stack.append([nums[ind],ind])

    return res


n = [4,5,1,2,3,6,4,1]
        
res = func4(n)
print(res)

    