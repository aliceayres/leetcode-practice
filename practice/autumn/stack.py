'''
Stack 栈
'''


class Stack:
    def __init__(self,size):
        self.stack = [None for i in range(size)]
        self.top = -1
        self.size = size

    def stack_empty(self):
        return self.top == -1

    def push(self,x):
        if self.top == self.size-1:
            raise Exception('stack upflow')
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.stack_empty():
            raise Exception("stack underflow")
        e = self.stack.pop(self.top)
        self.top -= 1
        return e

if __name__ == '__main__':
    stack = Stack(10)
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