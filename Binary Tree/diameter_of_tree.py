def diameterOfBinaryTree(root):

    res = 0
    def dfs(curr):
        nonlocal res
        if not curr:
            return 0
        

        left = dfs(curr.left)
        right = dfs(curr.right)
        res = max(res, left + right)


        return max(left, right) + 1
    
    dfs(root)
    return res
