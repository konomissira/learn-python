class Node:
    def __init__(self, value):
        self.value  = value
        self.next = None

def find(node, element):
    while node:
        if(node.value == element):
            return True
        node = node.next
    return False;

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    

    print(find(head, 3))
    print(find(head, 6))
    print(find(head, 9))