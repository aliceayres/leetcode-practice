'''
Deque 双端队列 10.1-4
'''


class Deque:
    def __init__(self,size):
        self.deque = [None for i in range(size)]
        self.size = size
        self.left = self.size - 1
        self.right = 0

    def lpush(self,x):
        if self.left == (self.right - 1) % self.size and self.deque[self.left] is not None:
            raise Exception('deque upflow left=%d,right=%d'% (self.left,self.right))
        self.deque[self.left] = x
        self.left = (self.left - 1) % self.size

    def lpop(self):
        index = (self.left + 1) % self.size
        e = self.deque[index]
        if e is None:
            raise Exception('deque underflow')
        self.deque[index] = None
        self.left = index
        return e

    def rpush(self,x):
        if self.right == (self.left + 1) % self.size and self.deque[self.right] is not None:
            raise Exception('deque upflow')
        self.deque[self.right] = x
        self.right = (self.right + 1) % self.size

    def rpop(self):
        index = (self.right - 1) % self.size
        e = self.deque[index]
        if e is None:
            raise Exception('deque underflow')
        self.deque[index] = None
        self.right = index
        return e

if __name__ == '__main__':
    dq = Deque(10)
    for i in range(1,6):
        dq.lpush(i)
    dq.rpush(8)
    print(dq.deque)
    print(dq.rpop())
    print(dq.rpop())
    print(dq.deque)
    print(dq.lpop())
    print(dq.lpop())
    print(dq.lpop())
    print(dq.lpop())
    print(dq.deque,dq.left,dq.right)
    # print(dq.rpop())
    for i in range(1,11):
        dq.lpush(i)
    print(dq.deque, dq.left, dq.right)
    print(dq.rpop())
    print(dq.rpop())
    # dq.rpush(9)
