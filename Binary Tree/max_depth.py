


def func(root):
    if not root:
        return 0
    return 1 + max(func(root.left), func(root.right))
