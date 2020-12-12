class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def addLast(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            tail = self.head
            while(tail.next):
                tail = tail.next

            tail.next = new_node

    def printLinkList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

    def linkListSize(self):
        curr = self.head
        while(curr):
            curr = curr.next
            self.size += 1
        return self.size

    def removeFirst(self):
        size = self.linkListSize()
        self.size = size
        if(size == 0):
            return print('List is empty')
        if(size == 1):
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.head.next
            self.size -= 1

    def getElementAt(self,index):
        self.size = self.linkListSize()
        if index > self.size:
            return print('Invalid INput')
        else:
            head = self.head
            for i in range(0,index):
                head = head.next
            return head.data


    def addFirst(self,value):
        new_node = Node(value)
        size = self.linkListSize()
        if size <= 0:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node

    def addAt(self,index,value):
        new_node = Node(value)
        size = self.linkListSize()
        if(index < 0 or index>size):
            return print('invalid args')
        elif index == 0:
            self.addFirst(value)
        elif index == size:
            self.addLast(value)
        else:
            head = self.head
            for i in range(1,index-1):
                head = head.next

            prev_node = head
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node

    def removeLast(self):
        size = self.linkListSize()
        if (size == 0):
            return print('List is empty')
        elif (size == 1):
            self.head = None
            self.tail = None
            self.size = 0
        else:
            head = self.head
            for i in range(1,self.size-1):
                head = head.next
            secondLast = head
            secondLast.next= None
            # head.next = None
    def reverseLinkList(self):

        prev = None
        curr = self.head
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

        # left = 0
        # right = self.linkListSize()-1
        #
        # while(left < right):
        #     leftNode = Node(self.getElementAt(left))
        #     rightNode =  Node(self.getElementAt(right))
        #
        #     temp = leftNode.data
        #     leftNode.data = rightNode.data
        #     rightNode.data = temp
        #     left +=1
        #     right -=1

    def removeAt(self,index):
        curr = self.head
        for i in range(0,index-1):
            if(curr):
                curr = curr.next
        curr.next = curr.next.next

    def removefromLast(self,index):
        slow = self.head
        fast = self.head
        print(self.tail)
        for i in range(0,index):
            fast = fast.next

        while(fast.next != None):
            fast = fast.next
            slow = slow.next

        return print(slow.data)

    def stackSize(self):
        return self.linkListSize()

    def stackPush(self,data):
        self.addFirst(data)

    def stackPop(self):
        self.removeFirst()

    def stackTop(self):
        return print(self.getElementAt(0))

    def queueSize(self):
        return print(self.linkListSize())

    def queueAdd(self,value):
        self.addLast(value)

    def queueRemove(self):
        self.removeFirst()

    def queuePeek(self):
        return print(self.getElementAt(0))

list = LinkedList()
list.addLast(4)
list.addLast(2)
list.addLast(5)
list.addLast(90)
list.addLast(6)

# list.removeFirst()
# list.linkListSize()
# list.printLinkList()
# list.getElementAt(5)
# list.addFirst(3)
# list.addAt(3,14)
# list.removeLast()
# list.reverseLinkList()
# list.removeAt(2)
# list.removefromLast(2)

# list.stackSize()
# list.stackPush(60)
# list.stackPop()
# list.stackTop()


# list.queueSize()
# list.queueAdd(100)
# list.queueRemove()
# list.queuePeek()

# list.printLinkList()



