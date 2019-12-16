'''
Bellman-ford 最短路径（存在负权环）
bellman-ford list all negative infinite 24.1-4 负无穷的点
bellman-ford list nodes in circle 24.6-6 列出负权环上的点
'''

from practice.autumn.graphconnected import Graph as G
import sys

class Node:
    def __init__(self,data,index,d=0):
        self.data = data
        self.index = index
        self.d = d
        self.p = None

    def info(self):
        return format('[data=%s,index=%d,d=%d,p=%s]' % (self.data,self.index,self.d,self.p.data))

class Edge:
    def __init__(self,u,v,weight):
        self.u = u
        self.v = v
        self.weight = weight

    def info(self):
        return format('[%s→%s=%d]' % (self.u,self.v,self.weight))

class ShortestPath:
    @staticmethod
    def bellmanford_all(graph,s):
        vl = len(graph.vertices)
        nodes = [Node(vt.data, vt.index, sys.maxsize) for vt in graph.vertices]
        nodes[s].d = 0
        nodes[s].p = nodes[s]
        edges = []
        for vt in graph.vertices:
            p = vt.next
            while p is not None:
                edges.append(Edge(vt.index, p.index, p.weight))
                p = p.next
        for i in range(vl - 1):
            relax = 0
            for ed in edges:
                if nodes[ed.v].d > nodes[ed.u].d + ed.weight:
                    nodes[ed.v].d = nodes[ed.u].d + ed.weight
                    nodes[ed.v].p = nodes[ed.u]
                    nodes[ed.v].ng = nodes[ed.v].d
                    relax += 1
            if relax == 0:
                break
        hasCircle = False
        circle = []
        first = -1
        for ed in edges:
            if nodes[ed.v].d > nodes[ed.u].d + ed.weight:
                hasCircle = True
                first = ed.v
        if hasCircle is True:
            for i in range(vl - 1):
                relax = 0
                for ed in edges:
                    if  nodes[ed.v].d != -sys.maxsize and nodes[ed.v].d > nodes[ed.u].d + ed.weight:
                        nodes[ed.v].d = -sys.maxsize
                        nodes[ed.v].p = nodes[ed.u]
                        relax += 1
                if relax == 0:
                    break
            circle = ShortestPath.bellmanford_circle(nodes,first)
        return nodes,circle

    @staticmethod
    def bellmanford_circle(nodes, first):
        cache = {}
        p = nodes[first]
        while cache.get(p.index) is None:
            cache[p.index] = p
            p = p.p
        head = p
        circle = [head]
        p = head.p
        while p.index != head.index:
            circle.append(p)
            p = p.p
        return circle

    @staticmethod
    def bellmanford(graph,s):
        vl = len(graph.vertices)
        nodes = [Node(vt.data,vt.index,sys.maxsize) for vt in graph.vertices]
        nodes[s].d = 0
        nodes[s].p = nodes[s]
        edges = []
        for vt in graph.vertices:
            p = vt.next
            while p is not None:
                edges.append(Edge(vt.index,p.index,p.weight))
                p = p.next
        for i in range(vl-1):
            relax = 0
            for ed in edges:
                if nodes[ed.v].d > nodes[ed.u].d + ed.weight:
                    nodes[ed.v].d = nodes[ed.u].d + ed.weight
                    nodes[ed.v].p = nodes[ed.u]
                    nodes[ed.v].ng = nodes[ed.v].d
                    relax += 1
            if relax == 0:
                break
        for ed in edges:
            if nodes[ed.v].d > nodes[ed.u].d + ed.weight:
                return False
        return True

if __name__ == '__main__':
    adjs = [[('a', 0), ('b', 6), ('c', 7)],
            [('b', 0), ('c', 4), ('e', -4), ('d', 5)],
            [('c', 0), ('d', -3), ('e', 9)],
            [('d', 0), ('b', -2)],
            [('e', 0), ('d', 7), ('a', 2)]]
    # adjs = [[('s', 0), ('a', 3), ('c', 5), ('e', 2)],
    #         [('a', 0), ('b', -4)],
    #         [('b', 0), ('g', 4)],
    #         [('c', 0), ('d', 6)],
    #         [('d', 0), ('c', -3), ('g', 8)],
    #         [('e', 0), ('f', 3)],
    #         [('f', 0), ('e', -6), ('g', 7)],
    #         [('g', 0),('h', -1)],
    #         [('h', 0),('i', 2)],
    #         [('i', 0)]]
    graph = G.generate_adjacency(adjs)
    graph.print()
    noCircle = ShortestPath.bellmanford(graph, 0)
    print('bellmanford all:')
    nodes,circle = ShortestPath.bellmanford_all(graph, 0)
    for t in nodes:
        print(t.info())
    print('bellmanford circle:')
    for t in circle:
        print(t.info())

