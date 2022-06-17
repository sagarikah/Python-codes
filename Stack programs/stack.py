# Implementation of Stack using Linked List


class Node:
    def __init__(self,value):
        self.data = value
        self.next = None



class Stack:
    def __init__(self):
        self.top = None


    def is_empty(self):
        return self.top == None


    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is None:
            return "Stack Empty"
        else:
            print(self.top.data)
            self.top = self.top.next       
            

    def peek(self):
        if self.top is None:
            return "Stack Empty"
        else:
            return self.top.data


    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next


    def size(self):
        count = 0
        temp = self.top

        while temp is not None:
            count += 1
            temp = temp.next

        print(count)
        

    
