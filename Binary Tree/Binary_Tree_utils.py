class BinaryTree:



    def __init__(self, value, left = None, right =None):
        self.left = left
        self.right = right
        self.value = value


    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:             
            if not self.right:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)


    def inorder_traversal(self, root):

        if root:
            self.inorder_traversal(root.left)
            print(root.value, end = " ")
            self.inorder_traversal(root.right)


    def preorder_traversal(self, root):

        if root:
            print(root.value, end = " ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value, end = " ")
        