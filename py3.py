def func(arr):
    

    fast = 0
    slow = 0
    k = len(arr)
    while k > 0:
        print("fast = ", fast)
        print("slow = ", slow)
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
        k -= 1




arr = [3,7,1,4,5,6,8,2,4]
func(arr)