from Binary_Tree_utils import BinaryTree


def lowestAncestor(root: BinaryTree, p: BinaryTree, q: BinaryTree)-> BinaryTree:
    
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
