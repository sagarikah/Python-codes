
# Sorting a stack in ascending order where the smallest element is in the bottom
# Input (top-bottom) stack :  40, 4, 10, 45, 50
# Output (top-bpttom) stack : 50, 45, 40, 10, 4




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
            

    def peek(self):
        if self.top is None:
            return "Stack Empty"
        else:
            return self.top.data


    def traverse(self):
        temp = self.top
        while temp is not None:
            data = temp.data
            temp = temp.next
            return data


    def size(self):
        count = 0
        temp = self.top

        while temp is not None:
            count += 1
            temp = temp.next

        return count


    def sort(in_stack):
       size= in_stack.size()

       while size > 1:
           i = in_stack.pop()
           #j = in_stack.pop()
           if i < in_stack.top.data:
               in_stack.push(i)

       print(in_stack.traverse())
               
           



in_stack = Stack()

out_stack = Stack()


        
