# def NextGreaterTemp(temps):


#     stack = []
#     res = [0] * len(temps)


#     for i,t in enumerate(temps):
#         start = i
#         while stack and stack[-1][1] < t:
#             index, temp = stack.pop()
#             res[index] = i - index
#             start = index
#         stack.append([start, t])

#     return res


# temps = [78,67,87,77,79,60]
# res = NextGreaterTemp(temps)
# print(res)




# def minNumber(nums, num):


#     l,r = 0, len(nums) - 1

#     res = nums[0]

#     while l < r:
#         mid = l + (r - l)//2
#         if nums[mid] == num:
#             return num
#         elif nums[mid] > num:
#             r = mid - 1
#             res = nums[mid]
#         else:
#             res = nums[mid]
#             l = mid + 1
#     return res


# nums = [1,4,6,8,11,13,15,17,19,20,22,23]

# res = minNumber(nums, 16)


# print(res)




# def largestReactangle(heights):



#     maxArea = 0

#     stack = []

#     for i, h in enumerate(heights): 
#         start = i
#         while stack and stack[-1][1] > h:
#             index, height = stack.pop()
#             maxArea = max(maxArea, h * (i - index))
#             start = index
#         stack.append([start, h])


#     for i,h in stack:
#         maxArea = max(maxArea, h * (len(heights) - i))

#     return maxArea

# heights = [1,2,3,4,3,3,3,5,3,5]
# res = largestReactangle(heights)
# print(res)



# def minWindowSub(s, t):
    
#     if len(t) > len(s):
#         return ""
#     sL = len(s)
#     tL = len(t)
#     ans = [-1, -1]
#     tRec = {}
#     for c in t:
#         tRec[c] = tRec.get(c, 0) + 1
#     need = len(tRec)
#     have = 0 
    
#     l = 0
#     window = {}
#     res = float("infinity")
#     for r in range(len(s)):
        
#         window[s[r]] = window.get(s[r], 0) + 1
#         if s[r] in tRec and window[s[r]] == tRec[s[r]]:
#             have += 1


#         while have == need:
#             if (r - l + 1) <= res:
#                 res = r - l + 1
#                 ans = [l, r]
#             window[s[l]] = window[s[l]] - 1
#             if s[l] in tRec and window[s[l]] < tRec[s[l]]:
#                 have -= 1
#             l += 1


#     left, right = ans
#     return s[left: right + 1] if res!=float("infinity") else ""

                    
            
# def dailyTemps(temps):
    


#     stack = []

#     res = [0] * len(temps)


#     for i, t in enumerate(temps):
#         while stack and stack[-1][1] < t:
#             index, temp = stack.pop()
#             res[index] = i - index
#         stack.append([i, t])


#     return res

# temps = [77,78,67,87,99,67,56,77,89,91]

# res = dailyTemps(temps)
# print(res)



def searchInRotatedSortedArray(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r: 
        mid = l + (r - l)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > nums[l]:
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


def findNextMaximum(nums, target, findMaximum = True):
    
    l = 0
    r = len(nums) - 1
    res = float('infinity') if findMaximum else float("-infinity")
    while l <= r:
        
        mid = l + (r - l)//2

        if nums[mid] == target:
            return nums[mid]
        
        if findMaximum:
            if nums[mid] > target:
                res = min(nums[mid], res)
                r = mid - 1
            else:
                l = mid + 1
            res = nums[mid]
        else:
            if nums[mid] < target:
                res = max(nums[mid], res)
                l = mid + 1
            else:
                r = mid - 1
        
            res = nums[mid]

    return res 



         



nums = [1,2,5,6,7,8,10,12,15,16,18]

res = findNextMaximum(nums, 11, False)
print(res)