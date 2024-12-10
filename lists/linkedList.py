class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def addFirst(self, e):
        newNode = Node(e)
        newNode.next = self.__head
        self.__head = newNode
        self.__size += 1

        if self.__tail == None:
            self.__tail = self.__head

    def addLast(self, e):
        newNode = Node(e)

        if self.__tail == None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next 
        self.__size += 1

    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index >= self.__size:
            self.addLast(e)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    def add(self, e):
        self.addLast(e)



class Node:
    def __init__(self, e):
        self.element = e
        self.next = None