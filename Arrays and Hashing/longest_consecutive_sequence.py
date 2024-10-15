def longConsecutiveSeq(nums):
    def checkSeq(n):
        seqLength = 0
        while n + seqLength in s:
            seqLength += 1
        return seqLength  
    longest = 0
    s = set(nums)
    for num in nums:
        if num - 1 in s:
            continue
        longest = max(longest, checkSeq(num))
    return longest


nums = [100,3,1,2,200,4,10,11,12,13,14,15,16]

res = longConsecutiveSeq(nums)
print(res)

    