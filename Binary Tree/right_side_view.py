from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rightSideView(root):
    d=defaultdict(int)
    def foo(x,depth):
        if x.left: foo(x.left,depth+1)
        # Right nodes will override the left nodes values.
        d[depth]=x.val
        if x.right: foo(x.right,depth+1)
    if root: foo(root,0)
    return [d[i] for i in sorted(d.keys())]