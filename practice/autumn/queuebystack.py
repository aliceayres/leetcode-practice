'''
两个栈实现队列 10.1-6
'''
from practice.autumn import stack as st

class QueueS:
    def __init__(self,size):
        self.push_stack = st.Stack(size)
        self.pop_stack = st.Stack(size)

    def print(self):
        print(self.push_stack.stack,self.pop_stack.stack)

    def enqueue(self,x):
        self.push_stack.push(x)
        return

    def dequeue(self):
        if self.pop_stack.stack_empty() is not True:
            return self.pop_stack.pop()
        while self.push_stack.stack_empty() is not True:
            self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()


if __name__ == '__main__':
    q = QueueS(10)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    q.print()