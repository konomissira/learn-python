class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end= " ")

root                   = Node(0)
root.left              = Node(1)
root.right             = Node(2)
root.left.left         = Node(3)
root.left.right        = Node(4)
root.right.left        = Node(5)
root.right.right       = Node(6)
root.left.left.left    = Node(7)
root.right.left.right  = Node(8)
root.right.right.right = Node(9)

def main():
    post_order(root)

main()