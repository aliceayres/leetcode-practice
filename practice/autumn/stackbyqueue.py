'''
两个队列实现栈 10.1-7
'''
from practice.autumn import queue as qu

class StackQ:
    def __init__(self,size):
        self.qu_1 = qu.Queue(size)
        self.qu_2 = qu.Queue(size)

    def print(self):
        print(self.qu_1.queue,self.qu_2.queue)

    def push(self,x):
        queue = self.qu_1
        queue_empty = self.qu_2
        if self.qu_1.isempty():
            queue_empty = self.qu_1
            queue = self.qu_2
        queue_empty.enqueue(x)
        while queue.isempty() is not True:
            queue_empty.enqueue(queue.dequeue())
        return

    def pop(self):
        queue = self.qu_1
        if self.qu_1.isempty():
            queue = self.qu_2
        return queue.dequeue()

if __name__ == '__main__':
    s = StackQ(10)
    s.push(3)
    s.push(1)
    print(s.pop())
    s.push(2)
    print(s.pop())
    print(s.pop())
