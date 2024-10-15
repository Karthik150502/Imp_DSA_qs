from collections import Counter
def func(s1, s2):
    
    if len(s1) > len(s2):
        return False

    s1Counter = [0] * 26
    s2Counter = [0] * 26
    s1len = len(s1)
    s2len = len(s2)
    for i in range(s1len):
        s1Counter[ord(s1[i]) - ord('a')] += 1
        s2Counter[ord(s2[i]) - ord('a')] += 1
    l = 0
    r = s1len - 1
    while r < s2len:
        if s1Counter == s2Counter:
            return True
        s2Counter[ord(s2[l]) - ord('a')] -= 1
        l += 1
        r += 1
        if r < s2len:
            s2Counter[ord(s2[r]) - ord('a')] += 1
    return False


print(func("ab","eidwaooo"))