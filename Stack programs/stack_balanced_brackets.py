# Program that checks wether a given mathematical expression is balanced 
# Balanced ->  (a+(b*c))
# Unbalanced ->  (a+(b*c)



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
            item = self.top.data
            self.top = self.top.next
            return item
            

    def peek(self):
        if self.top is None:
            return "Stack Empty"
        else:
            return self.top.data


    def size(self):
        count = 0
        temp = self.top

        while temp is not None:
            count += 1
            temp = temp.next

        return count



def brackets(expr):

    s = Stack()

    for i in expr:
        if i == '(' or i == '{' or i == '[':
            s.push(i)
            
        elif i == ')':
            if not handle_closing_bracket('(',s):
               return False
            
        elif i == '}':
          if not handle_closing_bracket('{',s):
            return False
        
        elif i == ']':
          if not handle_closing_bracket('[',s):
            return False
            

    if s.size() == 0:
        return True
    else:
        return False


def handle_closing_bracket(bracket_type, s):

  if s.size() == 0:
    return False

  else:
    if s.peek() == bracket_type:
      s.pop()
      return True
    else:
      return False
