def func(nums):

    m = nums[0]
    mi = 0
    for i in range(1,len(nums)):
        if nums[i] > m:
            m = nums[i]
            mi = i

    
    nums.pop(mi)

    sm = nums[0]
    for i in range(1, len(nums)):

        if nums[i] > sm and sm <= m:
            sm = nums[i]

    return m, sm, nums


nums = [1,2,3,14,31,53,5,54,43,32,32,3]
res = func(nums)
print(res)