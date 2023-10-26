class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
class Stack:
    def __init__(self):
        self.end = None

    def pop(self):

        if self.end is None:
            return IndexError

        pop_item = self.end
        self.end = self.end.pref
        pop_item.pref = None
        val = pop_item.data

        return val

    def push(self, val):
        node = Node(val)

        if self.end is None:
            self.end = node
        else:
            node.pref = self.end
            self.end = node

        pass

    def print(self):
        total = self.end
        if self.end is None:
            return Exception
        else:
            while total:
                print(total.data)
                total = total.pref

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()