def validPalindrome(s):
    def checkChar(c):
        return ord(c) >= ord("a") and ord(c) <= ord("z") or \
        ord(c) >= ord("0") and ord(c) <= ord("9") or \
        ord(c) >= ord("A") and ord(c) <= ord("Z")
    i,j = 0, len(s) - 1
    while i < j:
        while i < j and not checkChar(s[i]):
            i += 1
        while j > i and not checkChar(s[j]):
            j -= 1
        if s[i].lower() == s[j].lower():
            i,j = i + 1, j - 1
        else:
            return False
    

    return True



s = 'A man, a plan, a canal panama'
print(validPalindrome(s))



    




