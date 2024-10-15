def search(nums: list[int], target: int) -> bool:

    l,r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l)//2

        if nums[mid] == target:
            return True


        if nums[mid] > nums[l]:
            if nums[mid] > target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        elif nums[mid] < nums[l]:            
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else: 
            l += 1

    return False

arr = [2,5,6,0,0,1,2]
res = search(arr, 0)
print(res)