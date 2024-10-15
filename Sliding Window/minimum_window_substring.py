def minimumWindowSubstring(s,t):

    sr = {}
    tr = {}

    lenS = len(s)
    lenT = len(t)
    if lenT > lenS:
        return ""

    for c in t:
        tr[c] = 1 + tr.get(c, 0)

    need = len(tr)
    have = 0

    l = 0
    res = float("infinity")
    ans = [-1, -1]
    for r in range(lenS):
        c = s[r]
        sr[c] = 1 + sr.get(c, 0)
        if c in tr and sr[c] == tr[c]:
            have += 1

        while have == need:
            if((r - l + 1) <= res):
                res = r - l + 1
                ans = [l,r]
            sr[s[l]] -= 1
            if s[l] in tr and sr[s[l]] < tr[s[l]]:
                have -= 1
            l += 1


    left, right = ans
    return s[left:right + 1] if res != float("infinity") else ""


s = "aa"
t = "aa"
res = minimumWindowSubstring(s,t)
print(res)

# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))