'''
Dijkstra 单源最短路径（无负权环）
'''

from practice.autumn.graphconnected import Graph as G
from practice.autumn.prioritymin import PriorityQueue as Q
from practice.autumn.prioritymin import Node as N
import sys

class Node:
    def __init__(self,data,index):
        self.data = data
        self.index = index
        self.d = 0
        self.p = None

    def info(self):
        return format('[data=%s,index=%d,d=%d,p=%s]' % (self.data,self.index,self.d,self.p.data))

class ShortestPath:
    @staticmethod
    def shortest_path(graph,s,v):
        path = []
        traversal = ShortestPath.dijkstra(graph,s)
        mapping = {traversal[i].index: i for i in range(len(traversal))}
        vertex = traversal[mapping[v]]
        if vertex.d == sys.maxsize:
            return None
        p = vertex
        while p.index != s:
            path.insert(0,p)
            p = p.p
        path.insert(0,p)
        return path

    @staticmethod
    def dijkstra(graph,s):
        traversal = []
        cache = {}
        queue = Q()
        nodes = [Node(vtx.data, vtx.index) for vtx in graph.vertices]
        for i in range(len(nodes)):
            if i != s:
                nodes[i].d = sys.maxsize
            else:
                nodes[i].d = 0
                nodes[i].p = nodes[i]
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
                    if un.data.d > node.d + p.weight:  # relax
                        un.data.d = node.d + p.weight
                        un.data.p = node
                        queue.decrease_key(un,un.data.d)
                    # queue.print_queue()
                p = p.next
        return traversal

if __name__ == '__main__':
    adjs = [[('a', 0), ('c', 5), ('b', 8)],
            [('b', 0), ('d', 13), ('e', 8), ('c', 4)],
            [('c', 0), ('b', 1)],
            [('d', 0), ('c', 5), ('f', 6)],
            [('e', 0), ('d', 11), ('f', 9)],
            [('f', 0), ('a', 7)]]
    graph = G.generate_adjacency(adjs)
    graph.print()
    print('----')
    tr = ShortestPath.dijkstra(graph,0)
    for t in tr:
        print(t.info())
    print('----')
    path = ShortestPath.shortest_path(graph,0,5)
    for p in path:
        print(p.info())
