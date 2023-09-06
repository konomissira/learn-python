class Node:
    def __init__(self, key):
        self.left  = None
        self.right = None
        self.value = key

def level_order_traversal(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
         print(queue[0].value, end= " ")

         node = queue.pop(0)

         if node.left:
             queue.append(node.left)

         if node.right:
             queue.append(node.right)

def pre_order(root):
    if root:
        print(root.value, end= " ")

        pre_order(root.left)

        pre_order(root.right)

def in_order(root):
    if root:
        in_order(root.left)

        print(root.value, end= " ")

        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)

        post_order(root.right)

        print(root.value, end= " ")


root             = Node(1)
root.left        = Node(2)
root.right       = Node(3)
root.left.left   = Node(4)
root.left.right  = Node(5)
root.right.left  = Node(6)
root.right.right = Node(7)



def main():
    level_order_traversal(root)
    print("Level-order traversal")
    pre_order(root)
    print("Pre-order traversal")
    in_order(root)
    print("In-order traversal")
    post_order(root)
    print("Post-order traversal")

main()