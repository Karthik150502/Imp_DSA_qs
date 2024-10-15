from Binary_Tree_utils import BinaryTree


def buildTree(postorder, inorder):


    if not postorder or not inorder:
        return

    root = BinaryTree(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.right = buildTree(postorder[mid: -1], inorder[mid + 1:]) 
    root.left = buildTree(postorder[:mid],  inorder[:mid]) 
    return root



postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]

res = buildTree(postorder, inorder)
res.inorder_traversal(res)
print()
res.postorder_traversal(res)
print()
res.preorder_traversal(res)
