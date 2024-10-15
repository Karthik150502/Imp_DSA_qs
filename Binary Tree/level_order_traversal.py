from Binary_Tree_utils import BinaryTree



def levelOrderTraversal(root):


    if not root: return []

    queue = [root]

    res = []
    while queue:
        temp = []

        qLen = len(queue)
        for _ in range(qLen):
            node = queue.pop(0)
            if node:
                temp.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        
        if temp:
            res.append(temp)

    return res



bin = BinaryTree(12)

bin.insert(10)
bin.insert(16)
bin.insert(9)
bin.insert(2)
bin.insert(1)
bin.insert(0)
bin.insert(21)
bin.insert(3)
bin.insert(-9)


res = levelOrderTraversal(bin)
print(res)