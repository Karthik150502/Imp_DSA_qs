def isSubtree(root, subRoot):



    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    
    if root.val == subRoot.val:
        return isSubtree(root.left, subRoot.left) and isSubtree(root.right, subRoot.right)
    else:
        return isSubtree(root.left, subRoot) and isSubtree(root.right, subRoot)