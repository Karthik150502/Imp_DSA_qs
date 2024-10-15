
def nextGreaterElement(nums1, nums2):

    hashMap = {n:i for i,n in enumerate(nums1)}

    res = [-1] * len(nums1)

    stack = [] 
    for num in nums2:

        while stack and stack[-1] < num:
            smaller_num = stack.pop()
            if smaller_num in hashMap:
                res[hashMap[smaller_num]] = num
        stack.append(num)

    return res



n1 = [4,1,2]
n2 = [1,3,4,2]
res = nextGreaterElement(n1, n2)

print(res)



def func(arr):

    stack = []
    res = [-1] * len(arr)

    for i,n in enumerate(arr):

        while stack and arr[stack[-1]] < n:
            index = stack.pop()
            res[index] = n
        stack.append(i)


    return res


arr = [1,2,4,2]
res = func(arr)
print(res)











