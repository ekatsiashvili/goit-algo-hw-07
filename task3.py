class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

# Test
root = Node(10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 20)

total_sum = sum_tree(root)
print("Сума всіх значень у дереві:", total_sum)