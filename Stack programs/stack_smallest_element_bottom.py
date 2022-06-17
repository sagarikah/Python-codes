##    Given a stack of integers, write a python program that updates the input stack such that all occurrences of the smallest values
##    are at the bottom of the stack, while the order of the other elements remains the same.
##
##        For example:
##        Input stack (top-bottom) :   5 66  5  8  7
##        Output:  66  8  7  5  5



class Stack:
    def __init__(self):
        self.items = list()
        self.top = 0

    def push(self,value):
        self.items.append(value)
        self.top += 1

    def pop(self):
        item = self.items[self.top]
        self.top -= 1
        return item

    def traverse(self):
       temp= self.top
       while self.top >= 0:
           print(self.items)
           self.top -= 1



        
