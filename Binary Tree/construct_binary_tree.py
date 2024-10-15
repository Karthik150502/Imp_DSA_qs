from Binary_Tree_utils import BinaryTree










def buildTree(preorder: list[int], inorder: list[int]) -> BinaryTree:
    

    if not preorder or not inorder:
        return None
    

    
    root = BinaryTree(preorder[0])
    mid = inorder.index(preorder[0])    
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root





preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

res = buildTree(preorder, inorder)
res.inorder_traversal(res)
res.preorder_traversal(res)