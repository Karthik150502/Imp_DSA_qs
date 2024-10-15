def isBalanced(root):
    def func(root):
        if not root: 
            return [True, 0]
        
        left = func(root.left) 
        right = func(root.right)
        isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 
        return [isBalanced, 1 + max(left[1], right[1])] 


    res = func(root)

    return res[0]