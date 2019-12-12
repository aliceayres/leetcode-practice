'''
Equivalent (simple) undirected graph of Multigraph o(v+e) 多图的等价简单无向图 22.1-4
delete repeated element from linked list o(n)
Square of directed graph 平方图（链表、矩阵） 22.1-5
Universal sink (in-degree = |v|-1 and out-degree = 0) 图的矩阵通用汇点 o(v)  22.1-6
Directed to undirected graph 有向图转无向图
'''
from practice.autumn.graphconnected import Node
from practice.autumn.graphconnected import GraphAdjLink as Gl
from practice.autumn.graphconnected import GraphAdjMatrix as Gm
from practice.autumn.graphconnected import Graph as G

class Solution:
    @staticmethod
    def is_universal_sink(matrix,k):
        for i in range(len(matrix)):
            if i != k and matrix[i][k] == 0:
                return False
            if matrix[k][i] != 0:
                return False
        return True

    @staticmethod
    def universal_sink(graph):
        i = 0
        j = 0
        while j < len(graph.matrix) and i < len(graph.matrix):
            if graph.matrix[i][j] == 0:  # prefer judge: out-degree = 0
                j += 1
            else:
                i += 1
        if i > len(graph.matrix): # find none of out-degree = 0
            return None
        else:
            if Solution.is_universal_sink(graph.matrix,i): # judge: in-degree = |v|-1
                return i
            else:
                return None

    @staticmethod
    def multi_undirgraph(multi):
        vertices = multi.vertices
        for head in vertices:  # |v|
            cache = {}
            pre = head
            p = head.next
            while p is not None: # degree → total |e|
                if p.data == head.data or cache.get(p.data) is not None:
                    pre.next = p.next
                    p = pre.next
                else:
                    cache[p.data] = 1
                    pre = p
                    p = p.next
        return Gl(vertices)

    @staticmethod
    def directed_undirgraph(graph):
        vertices = [p for p in graph.vertices]
        for i in range(len(graph.vertices)):
            head = graph.vertices[i]
            p = head.next
            while p is not None:
                t = graph.vertices[p.index].next
                pre = vertices[p.index]
                node = Node(head.data, head.index, p.weight)
                node.next = pre.next
                pre.next = node
                p = p.next
        return Solution.multi_undirgraph(Gl(vertices))

    @staticmethod
    def squre_graph_matrix(graph):
        matrix = []
        for i in range(len(graph.matrix)):
            row = [0 for i in range(len(graph.matrix))]
            for j in range(len(graph.matrix)):
                if graph.matrix[i][j] != 0:
                    for k in range(len(graph.matrix)):
                        if graph.matrix[j][k] > 0:
                            row[k] = 1
            matrix.append(row)
        return Gm(graph.vertices,matrix)

    @staticmethod
    def square_graph(graph):
        vertices = [Node(p.data,p.index,p.weight) for p in graph.vertices]
        for i in range(len(graph.vertices)):
            pre = vertices[i]
            head = graph.vertices[i]
            p = head.next
            while p is not None:
                t = graph.vertices[p.index].next
                while t is not None:
                    node = Node(t.data,t.index,t.weight)
                    node.next = pre.next
                    pre.next = node
                    t = t.next
                    pre = node # insert by tail
                p = p.next
        return  Solution.multi_undirgraph(Gl(vertices))

if __name__ == '__main__':
    adjs = [[('a', 0), ('c', 1), ('b', 1), ('a', 0), ('b', 1)],
            [('b', 0), ('d', 1)],
            [('c', 0), ('b', 1)],
            [('d', 0), ('c', 1), ('d', 1), ('c', 0), ('c', 1), ('f', 1)],
            [('e', 0), ('d', 1), ('d', 1), ('f', 0), ('f', 1)],
            [('f', 0), ('f', 0)]]
    multi = G.generate_adjacency(adjs)
    multi.print()
    result = Solution.multi_undirgraph(multi)
    result.print()
    square = Solution.square_graph(result)
    square.print()
    m = result.transform_matrix()
    m.print()
    squarem = Solution.squre_graph_matrix(m)
    squarem.print()
    vs = [i for i in range(4)]
    matrix = [[0,0,1,0],
              [0,0,0,0],
              [1,1,0,0],
              [1,1,0,1]]
    graph = Gm(vs,matrix)
    sink = Solution.universal_sink(graph)
    print(sink)