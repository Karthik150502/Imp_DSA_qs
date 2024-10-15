from collections import Counter
#Solution number 1, Time = O(n), Space = O(n)
def isAnagram1(s,t):
    if len(s) != len(t):
        return False
    hashMapS = {}
    hashMapT = {}

    for i in range(len(s)):
        hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
        hashMapT[t[i]] = 1 + hashMapT.get(t[i], 0)
    for key in hashMapS:
        if hashMapS[key] != hashMapT.get(key, 0):
            return False

    return True 

#Solution number 2, Time = O(nlogn), Space = O(n)
def isAnagram2(s,t):
    return sorted(s) == sorted(t)

#Solution number 3
def isAnagram3(s,t):
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"

print(isAnagram1(s, t))
print(isAnagram1(s, t))
print(isAnagram1(s, t))
