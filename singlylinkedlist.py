# Create nodes 
# Create linked list 
# Add nodes to linked list 
# Print linked list 


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        # head => Jake----pointsto---->NONE
        if self.head is None:
            self.head = newNode
        else:
            # head=>Jake->Ben->None || Jake -> Matthew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printlist(self):
        # head =>Jake-->Ben--->Matthew-->None
        if self.head is None: 
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

# Node => data,next
# firstNode.data => Jake, firstNode.next => None
firstNode = Node("Jake")
linkedList = LinkedList()
#linkedList.insert(firstNode)
secondNode = Node("Ben")
#linkedList.insert(secondNode)
thirdNode =  Node("Matthew")
#linkedList.insert(thirdNode)
linkedList.printlist()
