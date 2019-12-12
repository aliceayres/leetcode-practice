'''
Minimum Spaning Tree for connected undirected graph 最小生成树（连通无向图）
based on Priority Queue → V * T extract-min + E * T decrease-key ，V-1 <= E <= V^2
Prim （Minimum Binary Heap）(V+E)lgV → ElgV
Prim （Array）V^2+E → V^2  23.2-2
'''

from practice.autumn.graphconnected import Graph as G
from practice.autumn.graphmultigraph import Solution as S
from practice.autumn.prioritymin import PriorityQueue as Q
from practice.autumn.prioritymin import Node as N
import sys

class SimpleQ():
    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    def insert(self,x): # o(1)
        x.index = len(self.queue)
        self.queue.append(x)
        return

    def decrease_key(self,x,k): # o(1)
        self.queue[x.index].priority = k
        return

    def exch(self, queue, i, j):
        t = queue[i]
        queue[i] = queue[j]
        queue[j] = t
        ix = queue[i].index
        queue[i].index = queue[j].index
        queue[j].index = ix

    def extract_min(self): # o(n)
        min = self.queue[0]
        index = 0
        for i in range(1,len(self.queue)):
            if self.queue[i].priority < min.priority:
                min = self.queue[i]
                index = i
        self.exch(self.queue,index,-1)
        self.queue.pop(-1)
        return min

class Node:
    def __init__(self,data,index):
        self.data = data
        self.index = index
        self.d = 0
        self.p = None

    def info(self):
        return format('[data=%s,index=%d,d=%d,p=%s]' % (self.data,self.index,self.d,self.p.data))

class MST:
    @staticmethod
    def prim(graph,s):
        traversal = []
        cache = {}
        # queue = SimpleQ()
        queue = Q()
        nodes = [Node(vtx.data, vtx.index) for vtx in graph.vertices]
        source = nodes[s]
        for i in range(len(nodes)):
            if i != s:
                nodes[i].d = sys.maxsize
            else:
                nodes[i].d = 0
                nodes[i].p = nodes[i]
            nodes[i].s = source
            qn = N(nodes[i], nodes[i].d)
            cache[nodes[i].index] = qn
            queue.insert(qn)
        # queue.print_queue()
        while queue.empty() is not True:
            min = queue.extract_min()
            # queue.print_queue()
            node = min.data
            traversal.append(node)
            cache[node.index] = None
            p = graph.vertices[node.index].next
            while p is not None:
                un = cache[p.index]
                if un is not None: # still in queue
                    if un.data.d > p.weight:  # relax
                        un.data.d = p.weight
                        un.data.p = node
                        queue.decrease_key(un,un.data.d)
                    # queue.print_queue()
                p = p.next
        return traversal

if __name__ == '__main__':
    adjs = [[('a', 0), ('b', 4), ('h', 8)],
            [('b', 0), ('c', 8), ('h', 11)],
            [('c', 0), ('i', 2), ('f', 4), ('d', 7)],
            [('d', 0), ('f', 14), ('e', 9)],
            [('e', 0)],
            [('f', 0), ('e', 10)],
            [('g', 0), ('f', 2)],
            [('h', 0), ('g', 1)],
            [('i', 0), ('g', 6)]]
    graph = G.generate_adjacency(adjs)
    graph.print()
    undir = S.directed_undirgraph(graph)
    undir.print()
    print('----')
    tr = MST.prim(undir,0)
    for t in tr:
        print(t.p.data,t.data,t.d)
