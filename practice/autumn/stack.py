'''
Stack 栈
'''


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def stack_empty(self):
        return self.top == -1

    def push(self,x):
        self.stack.append(x)
        self.top += 1

    def pop(self):
        if self.stack_empty():
            raise Exception("stack underflow")
        e = self.stack.pop(self.top)
        self.top -= 1
        return e

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