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





class Node:
    def __init__(self, e):
        self.element = e
        self.next = None