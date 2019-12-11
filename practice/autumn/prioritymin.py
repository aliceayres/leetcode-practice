'''
Priority Queue by Min Binary Heap
基于最小堆的优先队列
'''
from practice.autumn import heap as hp
import sys

class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        self.index = 0  # relative index

    def __str__(self):
        return format('data=%s,priority=%d,index=%d' % (self.data,self.priority,self.index))

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.heap = hp.Heap()

    def print_queue(self):
        for e in self.queue:
            print(e)

    def insert(self,x):
        k = x.priority
        x.priority = sys.maxsize
        x.index = len(self.queue)
        self.queue.append(x)
        self.decrease_key(x,k)
        return

    def decrease_key(self,x,k):
        self.decrease_key_by_index(x.index, k)

    def minimum(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def min_heapify(self,i): # lgh
        length = len(self.queue)
        largest = i
        l = self.heap.left(i)
        r = self.heap.right(i)
        if l < length and self.queue[l].priority <= self.queue[i].priority:
            largest = l
        if r < length and self.queue[r].priority <= self.queue[largest].priority:
            largest = r
        if largest != i:
            self.exch(self.queue,largest,i)
            self.min_heapify(largest)

    def exch(self, queue, i, j):
        t = queue[i]
        queue[i] = queue[j]
        queue[j] = t
        ix = queue[i].index
        queue[i].index = queue[j].index
        queue[j].index = ix

    def extract_min(self):
        if len(self.queue) == 0:
            return None
        min = self.queue[0]
        self.exch(self.queue, 0, -1)
        self.queue.pop(-1)
        self.min_heapify(0)
        return min

    def decrease_key_by_index(self,idx,k):
        parent = self.heap.parent(idx)
        i = idx
        self.queue[idx].priority = k
        while parent >= 0 and self.queue[parent].priority > k:
            self.exch(self.queue,i,parent)
            i = parent
            parent = self.heap.parent(parent)
        return

if __name__ == '__main__':
    pq = PriorityQueue()
    num = [("a",7),("b",9),("c",11),("d",2),("e",16),("f",5),("g",8),("h",3),("i",4),("j",1)]
    cache = {}
    for e in num:
        node = Node(e[0],e[1])
        pq.insert(node)
        cache[node.data] = node
    pq.print_queue()
    print("extract_min",pq.extract_min())
    pq.print_queue()
    print("minimum",pq.minimum())
    pq.decrease_key(cache['e'],13)
    pq.print_queue()