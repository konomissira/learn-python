class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def find(root, key):
    if not root:
        return None
    if key == root.key:
        return root
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)
    
root = Node(10)
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 30)

node = find(root, 20)
print(node.key if node else "Not found")

node = find(root, 35)
print(node.key if node else "Not found")