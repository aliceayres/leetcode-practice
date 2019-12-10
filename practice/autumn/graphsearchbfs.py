'''
Breadth first search 广度优先搜索
BFS for linked list
Print path from v to s
BFS for matrix 22.2-4
'''
from practice.autumn.graphconnected import Graph as G
from practice.autumn.queue import Queue as Q

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
    def get_bfs_path(graph,s,v):
        path = []
        traversal = Search.bfs_source(graph,s)
        mapping = {traversal[i].index:i for i in range(len(traversal))}
        vertex = traversal[mapping[v]]
        p = vertex
        while p.index != s:
            path.append(p)
            p = p.p
        path.append(p)
        return path

    @staticmethod
    def bfs(graph):
        traversal = []
        nodes = [Node(vtx.data,vtx.index) for vtx in graph.vertices]
        queue = Q(len(nodes))
        for i in range(len(nodes)):
            if nodes[i].color == 'white':
                source = nodes[i]
                nodes[i].color = 'grey'
                nodes[i].p = nodes[i]
                nodes[i].d = 0
                nodes[i].s = source
                queue.enqueue(nodes[i])
                node = queue.dequeue()
                while node is not None:
                    p = graph.vertices[node.index].next
                    while p is not None:
                        if nodes[p.index].color == 'white':
                            nodes[p.index].color = 'grey'
                            nodes[p.index].p = node
                            nodes[p.index].d = node.d + 1
                            nodes[p.index].s = source
                            queue.enqueue(nodes[p.index])
                        p = p.next
                    node.color = 'black'
                    traversal.append(node)
                    node = queue.dequeue()
        return traversal

    @staticmethod
    def bfs_source(graph,s):
        traversal = []
        nodes = [Node(vtx.data, vtx.index) for vtx in graph.vertices]
        queue = Q(len(nodes))
        nodes[s].color = 'grey'
        nodes[s].p = nodes[s]
        nodes[s].d = 0
        source = nodes[s]
        nodes[s].s = source
        queue.enqueue(nodes[s])
        node = queue.dequeue()
        k = 0
        while node is not None:
            p = graph.vertices[node.index].next
            while p is not None:
                if nodes[p.index].color == 'white':
                    nodes[p.index].color = 'grey'
                    nodes[p.index].p = node
                    nodes[p.index].d = node.d + 1
                    nodes[p.index].s = source
                    queue.enqueue(nodes[p.index])
                p = p.next
            node.color = 'black'
            traversal.append(node)
            node = queue.dequeue()
            if node is None:
                while k < len(nodes):
                    if nodes[k].color == 'white':
                        nodes[k].color = 'grey'
                        nodes[k].p = nodes[k]
                        nodes[k].d = 0
                        source = nodes[k]
                        nodes[k].s = source
                        queue.enqueue(nodes[k])
                    k += 1
                node = queue.dequeue()
        return traversal

    @staticmethod
    def bfs_source_matrix(graph,s):
        traversal = []
        nodes = [Node(graph.vertices[i], i) for i in range(len(graph.vertices))]
        queue = Q(len(nodes))
        nodes[s].color = 'grey'
        nodes[s].p = nodes[s]
        nodes[s].d = 0
        source = nodes[s]
        nodes[s].s = source
        queue.enqueue(nodes[s])
        node = queue.dequeue()
        k = 0
        while node is not None:
            out = graph.matrix[node.index]
            for i in range(len(out)):
                if out[i] != 0 and nodes[i].color == 'white':
                    nodes[i].color = 'grey'
                    nodes[i].p = node
                    nodes[i].d = node.d + 1
                    nodes[i].s = source
                    queue.enqueue(nodes[i])
            node.color = 'black'
            traversal.append(node)
            node = queue.dequeue()
            if node is None:
                while k < len(nodes):
                    if nodes[k].color == 'white':
                        nodes[k].color = 'grey'
                        nodes[k].p = nodes[k]
                        nodes[k].d = 0
                        source = nodes[k]
                        nodes[k].s = source
                        queue.enqueue(nodes[k])
                    k += 1
                node = queue.dequeue()
        return traversal

if __name__ == '__main__':
    adjs = [[('a', 0), ('c', 1), ('b', 1)],
            [('b', 0), ('d', 1)],
            [('c', 0), ('b', 1)],
            [('d', 0), ('c', 1), ('f', 1)],
            [('e', 0), ('d', 1), ('f', 1)],
            [('f', 0), ('a', 1)]]
    graph = G.generate_adjacency(adjs)
    graph.print()
    print('----')
    t1 = Search.bfs(graph)
    for t in t1:
        print(t.info())
    print('----')
    t2 = Search.bfs_source(graph, 0)
    for t in t2:
        print(t.info())
    print('----')
    t3 = Search.bfs_source(graph, 3)
    for t in t3:
        print(t.info())
    print('----')
    t4 = Search.bfs_source_matrix(graph.transform_matrix(), 3)
    for t in t4:
        print(t.info())
    print('----')
    path = Search.get_bfs_path(graph,0,5)
    for t in path:
        print(t.info())
