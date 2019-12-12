'''
Minimum Spaning Tree for connected undirected graph 最小生成树（连通无向图）
Kruskal
based on disjoint set forest
'''

from practice.autumn.graphconnected import Graph as G
from practice.autumn.graphmultigraph import Solution as S
from practice.autumn.prioritymin import PriorityQueue as Q
from practice.autumn.prioritymin import Node as QN
from practice.autumn.disjointsetforest import DisjointSet as DS

class Edge:
    def __init__(self,u,udata,v,vdata,weight):
        self.u = u
        self.udata = udata
        self.v = v
        self.vdata = vdata
        self.weight = weight

    def info(self):
        return format('[%s→%s=%d]' % (self.udata,self.vdata,self.weight))

class MST:
    @staticmethod
    def kruskal(graph): # graph is represented as undir-single graph
        mst = []
        sets = [DS.make_set(node) for node in graph.vertices]
        queue = Q()
        for head in graph.vertices:
            p = head.next
            while p is not None:
                e = Edge(head.index,head.data,p.index,p.data,p.weight)
                queue.insert(QN(e,p.weight))
                p = p.next
        while queue.empty() is not True:
            mine = queue.extract_min().data
            if DS.find_set(sets[mine.u]) != DS.find_set(sets[mine.v]):
                DS.union(sets[mine.u],sets[mine.v])
                mst.append(mine)
        return mst

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
    S.undirgraph_single(undir)
    undir.print()
    print('----')
    tr = MST.kruskal(undir)
    for t in tr:
        print(t.info())
