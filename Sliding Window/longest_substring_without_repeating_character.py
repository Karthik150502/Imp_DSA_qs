# Neetcode solution
def lengthOfLongestSubstring(s):

    charSet = set()

    res = 0
    l = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res



s = "abcabcbb"
s = " "
res = lengthOfLongestSubstring(s)
print(res)
        



# My solution
def lengthOfLongestSubstring(s):

    hash = dict()
    res = 0
    l = 0
    for r in range(len(s)):
        while s[r] in hash and hash[s[r]] >= l:
            l = hash[s[r]] + 1
            del hash[s[r]]
        hash[s[r]] = r
        res = max(res, r - l + 1)
    return res





test = [
    {"ip":"","op":0},
    {"ip":"a","op":1},
    {"ip":"aaa","op":1},
    {"ip":" ","op":1},
    {"ip":"abcdefgabcdefgabcdefghiabcdefgabcdefgh","op":9},
    {"ip":"pwwkew","op":3},
    {"ip":"abcabcdabc","op":4},
]


result = map(lambda x: lengthOfLongestSubstring(x["ip"]) == x["op"], test)
print("All Tests passed" if all(result) else "Test/s failed." )



