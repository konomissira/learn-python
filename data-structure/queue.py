class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.back  = None

    def enqueue(self, item):
        newnode = Node(item)
        if self.back is None:
            self.front = self.back = newnode
            return
        self.back.next = newnode
        self.back = newnode
    def dequeue(self):
        if self.is_empty():
            return None
        current = self.front
        self.front = current.next
        if self.front is None:
            self.back = None
        return current.data
    def is_empty(self):
        return self.front is None
    
    def front_item(self):
        if not self.is_empty():
            return self.front.data
        return None
    
    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
    

my_queue = QueueLinkedList()
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(6)
my_queue.enqueue(8)
my_queue.enqueue(10)

print(my_queue.dequeue())
print(my_queue.front_item())
print(my_queue.size())