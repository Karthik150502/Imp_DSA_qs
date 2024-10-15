def func(s):
    res = [""]    
    for r in range(len(s) + 1):
        l = 0
        temp = []
        while l < r:
            temp.append(s[l:r])
            l += 1
        res.extend(temp.copy())
    return res


s = "AABBA"
res = func(s)
print(res)