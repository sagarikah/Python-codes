# Linked List implementation


class Node:     # creates a node

    def __init__(self,value):
        self.data = value
        self.next = None


class LL:

    def __init__(self):
        self.head = None


    def add(self, value):        # inserts from head

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def add_tail(self, value):

        new_node = Node(value)

        if self.head is None:
            


    def traverse(self):      # prints the linked list

        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        
