class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
        self.left = None


    def addLast(self,value):

        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.size += 1
            return
        else:
            head = self.head
            while(head.next):
                head = head.next

            head.next = new_node
            self.size += 1
            self.tail = new_node

    def printLinkList(self):
        curr = self.head
        while(curr):
            print(curr.data, end=" ")
            curr = curr.next

    def linkListSize(self):
        curr = self.head
        while(curr):
            curr = curr.next
            self.size += 1
        return self.size

    def removeFirst(self):
        if(self.size == 0):
            return print('List is empty')
        if(self.size == 1):
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.head.next
            self.size -= 1

    def getFirst(self):
        return self.head.data

    def getElementAt(self,index):
        self.size = self.linkListSize()
        if index > self.size:
            return print('Invalid INput')
        else:
            head = self.head
            for i in range(0,index):
                head = head.next
            return head


    def addFirst(self,value):

        new_node = Node(value)
        if self.size == 0:
            self.head = self.tail = new_node
            self.head.next = None
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

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
        for i in range(0,index):
            fast = fast.next

        while(fast.next != None):
            fast = fast.next
            slow = slow.next

        return print(slow.data)

    def getMiddleNode(self):
        slow = self.head
        fast = self.head

        while(fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
        return print(slow.data)

    def oddEven(self):
        odd = LinkedList()
        even = LinkedList()
        head = self.head
        while(head != None):
            if(head.data % 2 == 0):
                even.addLast(head.data)
                self.removeFirst()
            else:
                odd.addLast(head.data)
                self.removeFirst()

            head = head.next
        odd.tail.next = even.head
        self.head = odd.head
        self.tail = even.tail
        return self.printLinkList()


    def merge2LinkedList(self,l1,l2):
        mergedList = LinkedList()
        head1 = l1.head
        head2 = l2.head

        while(head1 != None and head2 !=None):
            if(head1.data < head2.data):
                mergedList.addLast(head1.data)
                head1 = head1.next
            else:
                mergedList.addLast(head2.data)
                head2 = head2.next

        while(head1 != None):
            mergedList.addLast(head1.data)
            head1 = head1.next

        while (head2 != None):
            mergedList.addLast(head2.data)
            head2 = head2.next

        mergedList.printLinkList()

    def midNode(self,head):
        slow = head
        fast = head

        while(fast != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return  slow

    # def mergeSort(self, head):
    #     if( head is None or head.next is None):
    #         new_list = LinkedList();
    #         new_list.addLast(head.data)
    #         return head
    #
    #     mid = self.midNode(head)
    #     nextToMid = mid.next
    #     mid.next = None
    #
    #     fsh = self.mergeSort(head)
    #     ssh = self.mergeSort(nextToMid)
    #     mergeSortedList =  LinkedList.merge2LinkedList(fsh,ssh)
    #     return mergeSortedList

    def removeDuplicates(self,listHead):
        while(listHead.next != None):
            if (listHead.data == listHead.next.data):
                listHead.next = listHead.next.next
            else:
                listHead = listHead.next
        return

    def Kreverse(self,k):
        prev = None
        while(self.size > 0):
            curr = LinkedList()
            if(self.size >= k):
                for i in range(1,k+1):
                    val = self.getFirst()
                    self.removeFirst()
                    curr.addFirst(val)
            else:
                currSize = self.size
                for i in range(1,currSize+1):
                    val = self.getFirst()
                    self.removeFirst()
                    curr.addLast(val)
            if(prev == None):
                prev = curr
            else:
                prev.tail.next = curr.head
                prev.tail = curr.tail
                prev.size += curr.size
        return prev.printLinkList()


    def displayreverseLinkListrecursive(self,node):
        if(node == None):
            return
        self.displayreverseLinkListrecursive(node.next);
        print(node.data, end=" ")

    def reversePointerHelper(self,node):
        if(node == None):
            return
        self.reversePointerHelper(node.next);
        if(node == self.tail):
            pass
        else:
            node.next.next = node
        return

    def reverselinkListbyPointerRecursion(self):
        self.reversePointerHelper(self.head)
        self.head.next = None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return self.printLinkList()

    def reverseDataHelper(self,right,floor):
        if(right == None):
            return
        self.reverseDataHelper(right.next,floor+1)

        if(floor > self.size/2):
            temp = right.data
            right.data = self.left.data
            self.left.data = temp

            self.left = self.left.next

    def reverseLinkListBydata(self):
        right = self.left = self.head

        self.reverseDataHelper(right,0)
        self.printLinkList()


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
list.addLast(2)
list.addLast(4)
list.addLast(5)
list.addLast(6)
list.addLast(90)

list2 = LinkedList()
list2.addLast(3)
list2.addLast(7)
list2.addLast(40)
list2.addLast(45)
list2.addLast(80)

list3 = LinkedList()
list3.addLast(90)
list3.addLast(8)
list3.addLast(3)
list3.addLast(6)
list3.addLast(5)
list3.addLast(63)
list3.addLast(92)
list3.addLast(20)

# list3.mergeSort(list3.head).printLinkList()
# list3.removeDuplicates(list3.head)
# list3.printLinkList()
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
# list.getMiddleNode()
# list.merge2LinkedList(list,list2)
# list3.oddEven()
# list3.Kreverse(3)
# list3.displayreverseLinkListrecursive(list3.head)
# list3.reverselinkListbyPointerRecursion()
list3.reverseLinkListBydata()

# list.stackSize()
# list.stackPush(60)
# list.stackPop()
# list.stackTop()


# list.queueSize()
# list.queueAdd(100)
# list.queueRemove()
# list.queuePeek()

# list.printLinkList()



