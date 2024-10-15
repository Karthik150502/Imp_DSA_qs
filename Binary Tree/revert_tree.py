from Binary_Tree_utils import BinaryTree
def invertTree(root: BinaryTree):


    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root
        
    


