'''
Graph connected components 图的连通分量
Graph adjacency linked list 图的邻接链表
Graph adjacency matrix 图的邻接矩阵
Graph transposition 图的转置 22.1-3
'''
from practice.autumn.disjointsetlinklist import DisjointSet as ds

class Node:
    def __init__(self,data,index=0,weight=0):
        self.data = data
        self.weight = weight
        self.index = index
        self.next = None

class GraphAdjMatrix():
    def __init__(self, vertices, matrix):
        self.vertices = vertices
        self.matrix = matrix

    def transpose(self):
        length = len(self.matrix)
        trmatrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                trmatrix[i][j] = self.matrix[j][i]
        return GraphAdjMatrix(self.vertices,trmatrix)

    def transform_linkedlist(self):
        llvertices = []
        for i in range(len(self.vertices)):
            head = Node(self.vertices[i],i)
            p = head
            line = self.matrix[i]
            for j in range(len(line)):
                if line[j] != 0:
                    node = Node(self.vertices[j],j,line[j])
                    p.next = node
                    p = node
            llvertices.append(head)
        return GraphAdjLink(llvertices)

    def print(self):
        print('---- graph adjacency matrix ----')
        print(self.vertices)
        for line in self.matrix:
            print(line)

class GraphAdjLink:
    def __init__(self, vertices):
        self.vertices = vertices

    def transform_matrix(self):
        mvertices = [vertex.data for vertex in self.vertices]
        matrix = []
        for vertex in self.vertices:
            line = [0 for i in range(len(self.vertices))]
            p = vertex.next
            while p is not None:
                line[p.index] = p.weight
                p = p.next
            matrix.append(line)
        return GraphAdjMatrix(mvertices,matrix)

    def transpose(self):
        trvertices = [Node(e.data,e.index,e.weight) for e in self.vertices]
        for i in range(len(self.vertices)):
            first = self.vertices[i]
            p = first.next
            while p is not None:
                head = trvertices[p.index]
                node = Node(first.data,i,p.weight)
                node.next = head.next
                head.next = node
                p = p.next
        return GraphAdjLink(trvertices)

    def print(self):
        print('---- graph adjacency linked list ----')
        for vertex in self.vertices:
            p = vertex
            while p is not None:
                print(p.data,'(',p.weight,p.index,')',end=' ')
                p = p.next
            print()

class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.components = None
        self.connected = None
        self.connected_component()
        return

    @staticmethod
    def generate_adjacency(adjs):
        vertices = []
        cache = {adjs[i][0][0]:i for i in range(len(adjs))}
        for vs in adjs:
            p = None
            for i in range(len(vs)):
                nd = Node(vs[i][0], cache[vs[i][0]], vs[i][1])
                if i == 0:
                    vertices.append(nd)
                    p = nd
                else:
                    p.next = nd
                    p = nd
        return GraphAdjLink(vertices)

    def print(self):
        print('---- graph components ----')
        for item in self.components.items():
            print(item[0],item[1],item[1].set)
        print('---- graph connected set ----')
        print(len(self.connected),self.connected)

    def connected_component(self):
        self.components = {}
        for vertex in self.graph.vertices:
            node = ds.make_set(vertex.data)
            self.components[vertex.data] = node
        for vertex in self.graph.vertices:
            vertexn = self.components[vertex.data]
            p = vertex.next
            while p is not None:
                pn = self.components[p.data]
                if ds.find_set(vertexn) != ds.find_set(pn):
                    ds.union(vertexn,pn)
                p = p.next
        self.connected = set([e[1].set for e in self.components.items()])

    def refresh_connected(self):
        self.connected = set([e[1].set for e in self.components.items()])
        return self.connected

    def same_component(self,x,y):
        return ds.find_set(self.components[x]) == ds.find_set(self.components[y])

if __name__ == '__main__':
    adjs = [[('a',0), ('c',1)],
            [('b',0), ('a',1), ('c',1)],
            [('c',0), ('b',1)],
            [('d',0), ('b',1)],
            [('e',0), ('f',1), ('g',1)],
            [('f',0)],
            [('g',0), ('e',1)],
            [('h',0), ('i',1)],
            [('i',0), ('h',1)],
            [('j',0)]]
    graph_al = Graph.generate_adjacency(adjs)
    graph_mx = graph_al.transform_matrix()
    graph_mx.print()
    graph_mx.transpose().print()
    graph_al2 = graph_mx.transform_linkedlist()
    graph_al.print()
    graph_al.transpose().print()
    graph_al2.print()
    graph = Graph(graph_al)
    graph.print()
    print(graph.same_component('a','g'))