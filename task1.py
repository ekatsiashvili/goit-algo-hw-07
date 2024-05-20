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

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Test
root = Node(10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 20)

max_value = find_max(root)
print("Найбільше значення у дереві:", max_value)
