def nextGreaterElement2(nums):

    N = len(nums)
    stack = []
    res = [-1] * N * 2
    for i in range(N * 2):
        n =  nums[i % N]
        while stack and stack[-1][1] < n:
            ind, num = stack.pop()
            res[ind] = n
        stack.append([i,n])
    return res[:N]

n = [4,5,1,2,3,6,4,1]
# [5, 6, 2, 3, 6, -1, 5, 4]

res = nextGreaterElement2(n)
print(res)