# def coinChange(arr, s):


#     res = []
#     m = float('infinity')
#     def recursiveFunc(arr, s, index = 0, r = []):
#         nonlocal m
#         if index == len(arr):
#             if s == 0:
#                 if len(r) < m:
#                     m = len(r)
#                 res.append(r.copy())
#             return
        
#         if arr[index] <= s:
#             r.append(arr[index])
#             recursiveFunc(arr, s - arr[index], index, r)
#             r.pop()
        
#         recursiveFunc(arr, s, index + 1, r)
#     recursiveFunc(arr, s)
#     return m if m != float('infinity') else -1




# arr = [1,2,5,3,4,6]
# t = 24

# res = coinChange(arr, t)
# print(res)



# def getSubsets(arr):


#     result = [[]]
#     def rec(arr, index = 0, res =[]):
#         for i in range(index, len(arr)):
#             res.append(arr[i])
#             result.append(res.copy())
#             rec(arr, i + 1, res)
#             res.pop()
    
#     rec(arr)
#     return result
            
# arr = [1,2,3,4]
# res = getSubsets(arr)
# print(res)



def func(arr):

    slow = 0
    fast = 0

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = arr[slow]
        slow2 = arr[slow2]
        if slow == slow2:
            return slow
        



arr = [1,3,2,4,4]
res = func(arr)
print(res)