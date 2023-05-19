#'Introduction to programming':Task 4
#Seryakov Vlad, FB-21, V-2(22)

class Node:
    def __init__(self, cargo=None, next=None, prev=None):
        self.cargo = cargo
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.cargo)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        
    def addFirst(self, e):
        node = Node(e)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        
    def addLast(self, e):
        node = Node(e)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        
    def add(self, index, e):
        node = Node(e)
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.addFirst(e)
        elif index == self.length:
            self.addLast(e)
        else:
            node = self.head
            for i in range(index):
                node = node.next
            newNode = Node(e, node, node.prev)
            node.prev.next = newNode
            node.prev = newNode
            self.length += 1
        
    def takeFirst(self):
        if self.length == 0:
            raise IndexError("List is empty")
        e = self.head.cargo
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return e
        
    def takeLast(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.tail.cargo
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return value
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.takeFirst()
        elif index == self.length - 1:
            self.takeLast()
        else:
            node = self.head
            for i in range(index):
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            
    def set(self, index, e):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        node = self.head
        for i in range(index):
            node = node.next
        node.cargo = e
        
    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        node = self.head
        for i in range(index):
            node = node.next
        return node.cargo
    
    def printReverse(self):
        node = self.tail
        while node is not None:
            print(node.cargo, end=' ')
            node = node.prev
            
    def __str__(self):
        node = self.head
        string = ''
        while node:
            string += str(node) + ' '
            node = node.next
        return string