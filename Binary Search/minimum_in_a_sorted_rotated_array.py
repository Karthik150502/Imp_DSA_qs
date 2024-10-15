def search(nums):
    # Press Alt+ Z in VS Code to revert thge text-wrap.z
    # Initialise for accessing elements from both ends
    l,r = 0, len(nums) - 1
    # Set the default value for the minimum value as the first value of the array, it doesnt matter.
    minnum = nums[0]
    # Traverse untill the left pointer is equal to or less than right pointer. 
    while l <= r:
        # If left pointer's value is less than that of the right pointer's value, then we have a sorted array, we can return the minimum of the previous minimum value and the value at the left pointer. 
        if nums[l] <= nums[r]:
            return min(minnum, nums[l])
        # Get the mid pointer from the left and the right pointer
        mid = l + (r - l) // 2
        
        # Update the minimum value.
        minnum = min(minnum, nums[mid])
        # If the value at the mid index is greater than or equal to the value at the left, then we are at the left portion of the array, where the nums are sorted. And since we had initially checked, if arr[l] <= arr[r], and that didn't comply, implied that the array has been rotated, therefore, we are now going to check the right half of the array, where, if the array has been rotated, we can find lesser values.
        if nums[mid] >= nums[l]:
            l = mid + 1
        # If the value at the mid is not greater then or equal to the left value, that would imply that, we are at the right portion of the array, where the nums are sorted, And we need to find for the lesser value in the left half of the array, since, we already have the minimum value from the right part of the array.  
        else:
            r = mid - 1 



arr = [4,5,6,8,10,11,-13,-12,-11,-10,-7,1,2,3]
res = search(arr)
print(res)