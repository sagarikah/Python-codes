# String reversal using Stack (Linked List implementation)


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
            data = self.top.data
            self.top = self.top.next
            return data



def string_reverse(string):
    
    s = Stack()
    for i in string:
        s.push(i)

    rev = ""
    while (not s.is_empty()):
        rev = rev + s.pop()

    return rev

   
