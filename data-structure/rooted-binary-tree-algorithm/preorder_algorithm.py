class Node:
    def __init__(self, value):
        self.left   = None
        self.right  = None
        self.value    = value

def pre_order(root):
    if root:
        print(root.value, end= " ")
        pre_order(root.left)
        pre_order(root.right)


root              = Node(1)
root.left         = Node(2)
root.right        = Node(3)
root.left.left    = Node(4)
root.left.right   = Node(5)
root.right.left   = Node(6)
root.right.right  = Node(7)

def main():
    pre_order(root)

main()