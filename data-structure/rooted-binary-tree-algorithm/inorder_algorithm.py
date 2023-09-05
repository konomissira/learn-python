class Node:
    def __init__(self, val):
        self.left   = None
        self.right  = None
        self.val    = val

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end= " ")
        in_order(root.right)

root              = Node(1)
root.left         = Node(2)
root.right        = Node(3)
root.left.left    = Node(4)
root.left.right   = Node(5)
root.right.left   = Node(6)
root.right.right  = Node(7)

def main():
    in_order(root)

main()