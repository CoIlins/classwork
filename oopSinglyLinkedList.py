from symtable import Class

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteFromBeginning(self):
        if self.head is None:
            return "The linked list is empty"
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            return "List is Empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next= None




    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def insertAtTheEnd(self, new_data):
        new_node  =Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()

if __name__== '__main__':
    llist = LinkedList()
    llist.insertAtTheBeginning("fox")
    llist.insertAtTheBeginning("brown")
    llist.insertAtTheBeginning("quick")
    llist.insertAtTheBeginning("The")


    llist.insertAtTheEnd("jumps")
    llist.deleteFromBeginning()
    llist.insertAtTheBeginning("A")
    llist.deleteFromEnd()


    llist.printLinkedList()
    llist.deleteFromEnd()
    llist.printLinkedList()










