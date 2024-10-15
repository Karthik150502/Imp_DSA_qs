def func(nums, target):
    

    l,r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l)//2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > nums[l]:
            if nums[mid] > target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        else:                
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


arr = [5,0,1,2,3,4]
res = func(arr, 0)
print(res)