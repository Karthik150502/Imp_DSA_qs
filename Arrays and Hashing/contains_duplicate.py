def containsDuplicate(nums):
    hashSet = set()

    for num in nums:
        if num in hashSet:
            return True
        else:
            hashSet.add(num)
    return False


arr = [1,2,3]
print(containsDuplicate(arr))