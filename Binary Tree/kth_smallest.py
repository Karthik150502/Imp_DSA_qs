from Binary_Tree_utils import BinaryTree





def func(root: BinaryTree, k: int):


    nodes = []
    n = 0

    curr = root
    while curr or nodes:


        while curr:
            nodes.append(curr)
            curr = curr.left


        curr = nodes.pop()
        n += 1
        if n == k:
            return curr.value
        curr = curr.right

    





bin = BinaryTree(9)
bin.insert(7)
bin.insert(10)
bin.insert(6)
bin.insert(8)
bin.insert(5)
bin.insert(5)
bin.insert(3)
bin.inorder_traversal(bin)


print()

