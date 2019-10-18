'''
Priority Queue
基于最大堆的优先队列
'''
from practice.autumn import heap as hp

class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return format('data=%s,priority=%s' % (str(self.data),str(self.priority)))

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.heap = hp.Heap()

    def print_queue(self):
        for e in self.queue:
            print(e)

    def insert(self,x):
        k = x.priority
        x.priority = -1
        self.queue.append(x)
        self.increase_key(len(self.queue)-1,k)
        return

    def maximum(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def max_heapify(self,i): # lgh
        length = len(self.queue)
        largest = i
        l = self.heap.left(i)
        r = self.heap.right(i)
        if l < length and self.queue[l].priority >= self.queue[i].priority:
            largest = l
        if r < length and self.queue[r].priority >= self.queue[largest].priority:
            largest = r
        if largest != i:
            self.heap.exch(self.queue,largest,i)
            self.max_heapify(largest)

    def extract_max(self):
        if len(self.queue) == 0:
            return None
        max = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop(-1)
        self.max_heapify(0)
        return max

    def increase_key(self,idx,k):
        parent = self.heap.parent(idx)
        i = idx
        self.queue[idx].priority = k
        while parent >= 0 and self.queue[parent].priority < k:
            self.heap.exch(self.queue,i,parent)
            i = parent
            parent = self.heap.parent(parent)
        return

if __name__ == '__main__':
    pq = PriorityQueue()
    num = [("a",7),("b",9),("c",11),("d",2),("e",6),("f",5),("g",8),("h",3),("i",4),("j",1)]
    for e in num:
        node = Node(e[0],e[1])
        pq.insert(node)
    pq.print_queue()
    print("max=",pq.extract_max())
    pq.print_queue()
    print("max=",pq.maximum())
    pq.increase_key(3,13)
    pq.print_queue()