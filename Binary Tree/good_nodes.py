from Binary_Tree_utils import BinaryTree

def func(root):
    
    
    nodes = 0
    def dfs(root, m = float("-infinity")):
        nonlocal nodes
        if not root:
            return 0
        
        if root.value >= m:
            nodes += 1
            

        dfs(root.left, max(m, root.value))
        dfs(root.right, max(m, root.value)) 
        


    dfs(root)
    return nodes



# bin = BinaryTree(3)
# bin.left = BinaryTree(1)
# bin.left.left = BinaryTree(3)
# bin.right = BinaryTree(4)
# bin.right.right = BinaryTree(5)
# bin.right.left = BinaryTree(1)



bin = BinaryTree(3)
bin.left = BinaryTree(3)
bin.left.left = BinaryTree(4)
bin.left.right = BinaryTree(2)


res = func(bin)
print(res)
