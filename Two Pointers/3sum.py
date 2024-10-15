def threeSum(nums):
    nums.sort()
    result = []
    for i in range(0,len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 
        j,k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                result.append([nums[i],nums[j],nums[k]])
                j += 1
                while nums[j - 1] == nums[j] and j < k:
                    j += 1
            elif sum > 0:
                k -= 1
            else:
                j += 1
    return result

arr = [1,4,5,-5,-7,0,-7,-1,2,20,-5]
[-5, -7, -7, 2, -1, 0, 1, 2, 4, 3, 20]
print(threeSum(arr))
