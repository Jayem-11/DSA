# queue with linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)


    def enqueue(self, value):
        new_val = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = new_val
            self.linkedList.tail = new_val

        else:
            self.linkedList.tail.next = new_val
            self.linkedList.tail = new_val

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode


    def peek(self):
        if self.isEmpty():
            return "The queue is empty"

        else:
            return self.linkedList.head


    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

        
cQ = Queue()
cQ.enqueue(1)
cQ.enqueue(2)
cQ.enqueue(3)
print(cQ)