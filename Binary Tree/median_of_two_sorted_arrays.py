def func(nums1, nums2):


    N1 = len(nums1)
    N2 = len(nums2)
    A, B = nums1, nums2
    if N2 < N1:
        A, B = nums2, nums1
    l,r = 0, len(A) - 1
    total = N1 + N2
    half = total // 2
    while True:

        mid = l + (r - l)//2
        mid2 = half - mid - 2

        Aleft = A[mid] if mid >= 0 else float("-infinity") 
        Bleft = B[mid2] if mid2 >= 0 else float("-infinty")
        ARight = A[mid + 1] if mid + 1 < len(A) else float("infinity")
        BRight = B[mid + 1] if mid + 1 < len(B) else float("infinity")

        if Aleft <= BRight and Bleft <= ARight:
            if total%2:
                return max(ARight, BRight)
            else:
                res = max(Aleft, Bleft) + min(ARight, BRight)
                return res / 2
        elif Aleft > BRight:
            r = mid - 1
        else: 
            l = mid + 1
