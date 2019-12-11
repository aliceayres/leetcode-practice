'''
Dijkstra 单源最短路径（无负权环）
'''

from practice.autumn.graphconnected import Graph as G
from practice.autumn.prioritymin import PriorityQueue as Q

class Node:
    def __init__(self,data,index):
        self.data = data
        self.index = index
        self.d = 0
        self.p = None
        self.s = None
        self.color = 'white'

    def info(self):
        return format('[data=%s,index=%d,d=%d,p=%s,s=%s,color=%s]' % (self.data,self.index,self.d,self.p.data,self.s.data,self.color))

class Search:
    @staticmethod
    def get_single_source_shortest_path(graph,s,v):
        path = []
        return path

    @staticmethod
    def dijkstra(graph,s):
        traversal = []
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
