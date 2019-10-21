'''
Queue 循环队列 10.1.4
'''


class Queue:
    def __init__(self, size):
        self.queue = [None for i in range(size)]
        self.size = size
        self.top = 0    # head
        self.tail = 0   # tail to put

    def isempty(self):
        if self.top == self.tail:
            return True

    def enqueue(self,x):
        if self.top == self.tail and self.queue[self.tail] is not None:
            raise Exception('queue upflow')
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.size
        return

    def dequeue(self):
        if self.queue[self.top] is None:
            raise Exception('queue underflow')
        head = self.queue[self.top]
        self.queue[self.top] = None
        self.top = (self.top + self.size + 1) % self.size
        return head


if __name__ == '__main__':
    q = Queue(10)
    # print(q.dequeue())
    num = ["a","b","c","d","e","f","g","h","i","j"]
    for e in num:
        q.enqueue(e)
    # q.enqueue('m')
    for i in range(8):
        print(q.dequeue())
    print(q.queue, q.top, q.tail)
    q.enqueue('m')
    q.enqueue('n')
    for i in range(3):
        print(q.dequeue())
    print(q.queue, q.top, q.tail)
    # print(q.queue,q.top,q.tail)
    # print(q.top)
    # print(q.tail)
    # q.enqueue('x')
    # print(q.queue,q.top,q.tail)
    # q.enqueue('y')

    # q.enqueue('x')
    # q.enqueue('y')
    # print(q.queue,q.top,q.tail)
    # print(q.dequeue())
    # print(q.dequeue())
    # q.enqueue('x')
    # print(q.queue,q.top,q.tail)
    # print(q.dequeue())





