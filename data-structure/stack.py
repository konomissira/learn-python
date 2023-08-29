class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        pop_data = self.top.value
        self.top = self.top.next
        return pop_data
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.value

my_stack = Stack()

my_stack.push(25)
my_stack.push(50)
my_stack.push(100)
my_stack.push(125)
my_stack.push(150)
my_stack.push(175)

print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
