'''
基于优先队列的FIFO队列 6.5-7
'''
from practice.autumn import priority as pr

import sys

class FIFOQueue:
    def __init__(self):
        self.min = sys.maxsize
        self.priority = pr.PriorityQueue()

    def enqueue(self,x):
        node = pr.Node(x,self.min)
        self.min -= 1
        self.priority.insert(node)
        return

    def dequeue(self):
        node = self.priority.extract_max()
        if node is not None:
            return node.data
        return None

if __name__ == '__main__':
    q = FIFOQueue()
    num = ["a","b","c","d","e","f","g","h"]
    for e in num:
        q.enqueue(e)
    for i in range(len(num)+1):
        print(q.dequeue())