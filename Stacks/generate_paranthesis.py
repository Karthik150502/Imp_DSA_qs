def generateParanthesis(n):
    result = []
    res = ''
    def func(openP = 0, closeP = 0):
        nonlocal res
        if openP == n and closeP == n:
            result.append(res)
            return
        
        if openP < n:
            res = res + "("
            func(openP + 1, closeP)
            res = res[:-1]
        if closeP < openP:
            res = res + ")"
            func(openP, closeP + 1)
            res = res[:-1]

    func()
    return result

res = generateParanthesis(3)
print(res)


