import collections
def func(nums, k):

    res = []
    queue = collections.deque() 
    l = r = 0

    while r < len(nums):

        while queue and nums[queue[-1]] < nums[r]:  
            queue.pop()

        queue.append(r)
        if queue[0] < l:
            queue.popleft()

        if (r + 1) >= k:
            res.append(nums[queue[0]])
            l += 1

        r += 1

    return res



nums = [1,3,-1,-3,5,3,6,7]
k = 3

res = func(nums, k)
print(res)




