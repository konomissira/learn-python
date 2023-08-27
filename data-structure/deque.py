class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None

    def insert_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def insert_back(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
        return temp.data

    def delete_back(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        temp = self.back
        self.back = self.back.prev
        if self.back is None:
            self.front = None
        else:
            self.back.next = None
        return temp.data

    def get_front(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        return self.front.data

    def get_back(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        return self.back.data

# Test the implementation
if __name__ == "__main__":
    dq = Deque()
    dq.insert_front(10)
    dq.insert_front(20)
    dq.insert_back(30)
    dq.insert_back(40)
    dq.insert_back(50)
    dq.insert_back(60)
    print(dq.get_front()) 
    print(dq.get_back()) 
    dq.delete_front()
    print(dq.get_front())
    dq.delete_back()
    print(dq.get_back())