class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
def insert(head, newnode, index):
    if index==0:
        newnode.next = head
        return newnode
    current = head
    position = 0
    while current and position < index - 1:
        current = current.next
        position = position + 1
    
    if not current:
        print("Index out of boiunds")
    else:
        newnode.next = current.next
        current.next = newnode
    return head

def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

print("original List")
print_list(head)

new_node = Node(4)
_new_node = Node(6)
head = insert(head, new_node, 2)
head = insert(head, _new_node, 4)

print("/**********************/")
print_list(head)