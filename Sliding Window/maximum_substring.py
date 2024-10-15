def maxVowels(s, k):
    l,res,cnt = 0,0,0
    vowels = {'a','e','i','o','u'}

    for r in range(len(s)):
        if s[r] in vowels:
            cnt += 1

        if (r - l + 1) >= k:
            res = max(res, cnt)
            if s[l] in vowels:
                cnt -= 1
            l += 1

    return res


res = maxVowels("leetcode", 3)
print(res)