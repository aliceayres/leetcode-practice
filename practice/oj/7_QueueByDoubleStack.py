'''
7. 用两个栈实现队列
题目描述：
用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。
'''

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack is None or len(self.stack) == 0:
            return None
        return self.stack.pop(-1)

    def push(self,x):
        self.stack.append(x)

    def is_empty(self):
        return self.stack is None or len(self.stack) == 0

class Queue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self,x):
        self.stack_in.push(x)

    def pop(self):
        if self.stack_out.is_empty():  # only empty need push
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

class Solution:
    def testQueue(self):
        numbers = [1, 2, 3, 4, 5]
        queue = Queue()
        for e in numbers:
            queue.push(e)
        x = queue.pop()
        while x is not None:
            print(x)
            x = queue.pop()
        return

slt = Solution()
slt.testQueue()
