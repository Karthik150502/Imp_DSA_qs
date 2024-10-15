from Binary_Tree_utils import BinaryTree


def preorder(root, cont):

    if not root:
        cont.append("N")
        return 
    cont.append(root.value)
    preorder(root.left,cont)
    preorder(root.right, cont)




def ser(root):
    res = []
    preorder(root, res)
    return ",".join(res)



def deserialize(s):

    nodes = s.split(",")
    i = 0

    def dfs():
        if nodes[i] == "N":
            i += 1
            return None
        node = BinaryTree(nodes[i])
        i += 1
        node.left = dfs()
        node.left = dfs()
        return node

    return dfs

    pass


bin = BinaryTree(5)
bin.insert(8)
bin.insert(4)
bin.insert(1)
bin.insert(0)
bin.insert(9)
bin.insert(11)
bin.insert(17)


res =  ser(bin)
print(res)