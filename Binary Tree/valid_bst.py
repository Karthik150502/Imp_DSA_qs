from Binary_Tree_utils import BinaryTree




def func(root):



    def valid(root, left, right):
        if not root: 
            return True
    
        if not (root.value > left and right > root.value):
            return False

    
        return valid(root.left,left, root.value) and valid(root.right,root.value, right)


    return valid(root, float("-infinity"), float("infinity"))


bin = BinaryTree(5)

res = func(bin)
print(res)