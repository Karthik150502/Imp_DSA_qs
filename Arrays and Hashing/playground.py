def func(nums):
        
    def checkSeq(n):
        length = 0
        while n + length in hashSet:
            length += 1
        return length



    hashSet = set(nums)
    longest = 0
    for num in nums:    
        if num - 1 in hashSet:
            continue
        else:
            longest = max(longest, checkSeq(num))


    return longest

nums = [1,0,2,4,5,6,8,9]


print(func(nums))
    
