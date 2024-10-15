def func(s):
    h = {}
    maxLetter = ""
    maxN = 0
    res = []
    for i in range(len(s)):
        h[s[i]] = h.get(s[i], 0) + 1
        if h[s[i]] > maxN:
            maxLetter = s[i]
        maxN = max(maxN,h[s[i]])
        res.append(maxLetter)
    return res

s = "asdasdfasfasddddddddasadsasd"
res = func(s)
print(res)

