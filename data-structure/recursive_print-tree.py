class Node:
    def __init__(self):
        self.label = None
        self.children = list()

def recursivePrint(node):
    if not node:
        return
    print(node.label)
    for child in node.children:
        recursivePrint(child)

root = Node()
root.label = 1

child1 = Node()
child1.label = 2

child2 = Node()
child2.label = 3

grand_child_1 = Node()
grand_child_1.label = 4

grand_child_2 = Node()
grand_child_2.label = 5

root.children.append(child1)
root.children.append(child2)

child1.children.append(grand_child_1)
child2.children.append(grand_child_2)

recursivePrint(root)
