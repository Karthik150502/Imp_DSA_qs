from time import sleep
# def func(arr, arr2):
    

#     res = []

#     i,j = 0,0

#     while i < len(arr) and j < len(arr2):
#         if arr[i] <= arr2[j]:
#             res.append(arr[i])
#             i+=1
#         else:
#             res.append(arr2[j])
#             j+=1

#     while i < len(arr):
#         res.append(arr[i])
#         i+=1

#     while j < len(arr2):
#         res.append(arr2[j])
#         j+=1

#     N = len(res)
#     mid = N//2
#     if N%2:
#         return res[mid]
#     else:
#         return (res[mid-1] + res[mid])/2

    
# arr = [1,2]
# arr2 = [3,4]

# res = func(arr, arr2)
# print(res)




def func(nums1, nums2):
    N1 = len(nums1)
    N2 = len(nums2)
    totalCount = N1 + N2
    half = totalCount//2
    A,B = nums1, nums2
    if N2 < N1:
        A,B = B,A
    l,r = 0, len(A) - 1
    while True:
        mid = l + (r - l)//2
        # if mid == 4, that means, five elements, that is 0,1,2,3,4, so 5 elements must be subtracted from the half value, say if the half value is 10, 10 - (4 + 1) = 5, to get five elements in an array, we will consider till index 4, since that will give us 5 elements, 0,1,2,3,4. To get the index of the array 2 that will give us five elements is 10 - (4 + 1) - 1, i.e., half - mid - 2. 
        mid2 = half - mid - 2

        ALeft = A[mid] if mid >= 0 else float("-infinity")
        ARight = A[mid + 1] if (mid + 1) < len(A) else float("infinity")
        BLeft = B[mid2] if mid2 >= 0 else float("-infinity")
        BRight = B[mid2 + 1] if (mid2 + 1) < len(B) else float("infinity")

        if ALeft <= BRight and BLeft <= ARight:
            if totalCount % 2:
                return min(ARight, BRight)
            return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
        elif ALeft > BRight:
            r = mid - 1
        else:
            l = mid + 1



a1 = [1,2,3,4,5,6,7,8,9,9]
a2 = [3,4,5,6,7,8,9,10,12,13]
res = func(a1, a2)
print(res)

#       [3, 6] | [8]
#    [1, 2, 5] | [5, 9, 10]
# if al1[-1] > a2r[0]:
    #          [3] | [6, 8]
    # [1, 2, 5, 5] | [9, 10]

#       [3, 5] | [5]
#    [1, 2, 6] | [8, 9, 10]
# if al2[-1] > a1r[0]:
    #    [3, 5, 5] | []
    #       [1, 2] | [6, 8, 9, 10]


# [3]
# [1, 2, 5, 5]
# [6, 8]
# [9, 10]

