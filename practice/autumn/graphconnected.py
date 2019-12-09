'''
Graph connected components 图的连通分量
'''
from practice.autumn.disjointsetlinklist import DisjointSet as ds

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class GraphAdj:
    def __init__(self,adjs):
        self.vertices = []
        self.components = None
        self.connected = None
        self.generate_adjacency(adjs)
        self.connected_component()
        return

    def generate_adjacency(self,adjs):
        for vs in adjs:
            p = None
            for i in range(len(vs)):
                nd = Node(vs[i])
                if i == 0:
                    self.vertices.append(nd)
                    p = nd
                else:
                    p.next = nd
                    p = nd

    def print(self):
        print('---- graph adjacency ----')
        for vertex in self.vertices:
            p = vertex
            while p is not None:
                print(p.data,end=' ')
                p = p.next
            print()
        print('---- graph components ----')
        for item in self.components.items():
            print(item[0],item[1],item[1].set)
        print('---- graph connected set ----')
        print(len(self.connected),self.connected)

    def connected_component(self):
        self.components = {}
        for vertex in self.vertices:
            node = ds.make_set(vertex.data)
            self.components[vertex.data] = node
        for vertex in self.vertices:
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
    adjs = [['a', 'b', 'c'],
            ['b', 'a', 'c', 'd'],
            ['c', 'a', 'b'],
            ['d', 'b'],
            ['e', 'f', 'g'],
            ['f', 'e'],
            ['g', 'e'],
            ['h', 'i'],
            ['i', 'h'],
            ['j']]
    graph = GraphAdj(adjs)
    graph.print()
    print(graph.same_component('a','g'))