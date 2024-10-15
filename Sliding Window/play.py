# Neetcode solution
def longestRepeatingCharacter(s,k):
    count = {}
    res = 0
    maxF = 0
    l = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxF = max(maxF, count[s[r]])

        while (r - l + 1) - maxF > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res

5 - 3  
s = "AABABXA"


'''
AABABX, len = 6, maxf = 3, check = F, l = 0, r = 5
ABABX, len = 5, maxf = 3, check = F, l = 1, r = 5



AABAB, l = 0, r = 4, len = 5, m = 3, (r - l + 1) - m = T
ABABX, l = 1, r = 5, len = 5, m = 3, (r - l + 1) - m = T



A, maxF = 1, maxLen = 1, {A:1} 
AA, maxF = 2, maxLen = 2, {A:2} 
AAB, maxF = 2, maxLen = 3, {A:2, B:1}  
AABA, maxF = 3, maxLen = 4, {A:3, B:1}  
AABAB, maxF = 3, maxLen = 5, {A:3, B:2}  
AABABX, maxF = 3, maxLen = 5, {A:3, B:2, X:1}  
ABABX, maxF = 3, maxLen = 5, {A:2, B:2, X:1}  

'''


k = 2

res = longestRepeatingCharacter(s,k)
print(res)



