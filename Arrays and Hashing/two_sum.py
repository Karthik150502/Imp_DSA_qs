def twoSum(nums, target):
    counter = {}
    possibilities = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in counter:
            possibilities.append((counter[nums[i]], i))
        else:
            counter[diff] = i
    return possibilities

nums = [1,2,5,6,4,7]
target = 7

print(twoSum(nums, target))