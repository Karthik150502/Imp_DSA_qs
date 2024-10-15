from Binary_Tree_utils import BinaryTree




def func(root):


    res = [root.value]
    def rec(root):

        if not root:
            return 0
        
        left = rec(root.left)
        right = rec(root.right)
        leftMax = max(0, left)
        rightMax = max(0, right)

        res[0] = max(res[0], leftMax + rightMax + root.value)
        return root.value + max(leftMax, rightMax)

    rec(root)
    return res[0]



bin = BinaryTree(-10)
bin.left = BinaryTree(9)
bin.right = BinaryTree(20)
bin.right.left = BinaryTree(15)
bin.right.right = BinaryTree(7)


res = func(bin)
print(res)