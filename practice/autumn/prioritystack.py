'''
基于优先队列的栈 6.5-7
'''
from practice.autumn import priority as pr

class Stack:
    def __init__(self):
        self.priority = pr.PriorityQueue()

    def push(self,x):
        max = 0
        maximum = self.priority.maximum()
        if maximum is not None:
            max = maximum.priority
        node = pr.Node(x,max+1)
        self.priority.insert(node)
        return

    def pop(self):
        node = self.priority.extract_max()
        if node is not None:
            return node.data
        return None

if __name__ == '__main__':
    stack = Stack()
    num = ["e","b","a"]
    for e in num:
        stack.push(e)
    print(stack.pop())
    print(stack.pop())
    stack.push("c")
    stack.push("d")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

