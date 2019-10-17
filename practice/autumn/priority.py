'''
Priority Queue
基于最大堆的优先队列
'''


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def get_queue(self):
        return self.queue

    def parent(self,i):
        # return (i-1)>>1
        return (i-1)//2

    def left(self,i):
        # return (i<<1)+1
        return 2*i+1

    def right(self,i):
        # return (i+1)<<1
        return 2*i+2

    def max_heapify(self, num, i, length=None):  # lgh
        if length is None:
            length = len(num)
        largest = i
        l = self.left(i)
        r = self.right(i)
        if l < length and num[l] >= num[i]:
            largest = l
        if r < length and num[r] >= num[largest]:  # this compare large and r!
            largest = r
        if largest != i:
            self.exch(num, largest, i)
            self.max_heapify(num, largest, length)

    def insert(self,x):
        self.queue.append(-1)
        self.increase_key(len(self.queue)-1,x)
        return

    def maximum(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def extract_max(self):
        if len(self.queue) == 0:
            return None
        max = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop(-1)
        self.max_heapify(self.queue,0)
        return max

    def increase_key(self,idx,k):
        parent = self.parent(idx)
        i = idx
        self.queue[idx] = k
        while parent >= 0 and self.queue[parent] < k:
            self.exch(self.queue,i,parent)
            i = parent
            parent = self.parent(parent)
        return

    def exch(self, num, a, b):
        t = num[a]
        num[a] = num[b]
        num[b] = t

if __name__ == '__main__':
    pq = PriorityQueue()
    num = [7,9,1,2,6,5,8,3,4,0]
    for e in num:
        pq.insert(e)
    print(pq.get_queue())
    print(pq.extract_max())
    print(pq.get_queue())
    print(pq.maximum())
    pq.increase_key(3,13)
    print(pq.get_queue())