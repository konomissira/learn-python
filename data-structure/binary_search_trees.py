#PRINTING THE ELEMENTS OF BINARY SEARCH TREES IN SORTED ORDER
class Node:
    def __init__(self, key):
        self.label      = key
        self.parent     = None
        self.leftChild  = None
        self.rightChild = None

def printedSorted(node):
    root = node

    if root is None:
        return
    printedSorted(root.leftChild)
    print(root.label)
    printedSorted(root.rightChild)

root                                 = Node("Cherry")
root.leftChild                       = Node("Apple")
root.rightChild                      = Node("Lemon")
root.rightChild.leftChild            = Node("Imbe")
root.rightChild.rightChild           = Node("Nectarine")
root.rightChild.rightChild.leftChild = Node("Mango")

def main():
    printedSorted(root)

main()
