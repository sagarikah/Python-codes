# Undo-Redo using Stack


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



def undo_redo(text, pattern):       # text -> string on which operations will be done
                                  # pattern -> string of the form 'uur','ur','uuu',etc
    u = Stack()
    r = Stack()

    for i in text:       # initially the elements of text are added to the stack u
        u.push(i)

    for i in pattern:
        if i == 'u':            # when u is encountered, the last element in stack u is popped
            data = u.pop()        # and is pushed in stack r 
            r.push(data)
        else:
            data = r.pop()      # when r is encountered, the last element in stack r is popped
            u.push(data)         # and is pushed in stack u

    res = ''
    while (not u.is_empty()):
        res = u.pop() + res

    print(res)
        
            
