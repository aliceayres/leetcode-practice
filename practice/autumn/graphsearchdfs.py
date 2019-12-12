'''
Depth first search 深度优先搜索
DFS recursive
DFS by stack
'''
from practice.autumn.graphconnected import Graph as G
from practice.autumn.stack import Stack

class Node:
    def __init__(self,data,index):
        self.data = data
        self.index = index
        self.d = 0
        self.f = None
        self.p = None
        self.color = 'white'

    def info(self):
        return format('[data=%s,index=%s,d=%s,f=%s,p=%s,color=%s]' % (self.data,self.index,self.d,self.f,self.p.data,self.color))


class DepthFirstGraph:
    def __init__(self,graph):
        self.graph = graph
        self.traversal = []
        self.nodes = [Node(vtx.data, vtx.index) for vtx in graph.vertices]
        self.time = 0
        self.parantheses = ''

    def dfs_stack(self):
        stack = Stack(len(self.nodes))
        for node in self.nodes:
            if node.color == 'white':
                self.time += 1
                node.d = self.time
                node.color = 'grey'
                if node.p is None:
                    node.p = node
                stack.push(node)
                self.traversal.append(node)
                self.parantheses += '(' + node.data
            while stack.stack_empty() is not True:
                node = stack.get_top()
                p = graph.vertices[node.index].next
                find = None
                while p is not None:
                    if self.nodes[p.index].color == 'white':
                        find = self.nodes[p.index]
                        break
                    p = p.next
                if find is None:
                    stack.pop()
                    node.f = self.time
                    self.parantheses += ')'
                    node.color = 'black'
                else:
                    find.p = node
                    self.time += 1
                    find.d = self.time
                    find.color = 'grey'
                    stack.push(find)
                    self.traversal.append(find)
                    self.parantheses += '(' + find.data

    def dfs(self):
        for node in self.nodes:
            if node.color == 'white':
                self.dfs_visit(node)

    def dfs_visit(self, node):
        self.time += 1
        node.d = self.time
        node.color = 'grey'
        if node.p is None:
            node.p = node
        self.traversal.append(node)
        self.parantheses += '('+ node.data
        p = graph.vertices[node.index].next
        while p is not None:
            if self.nodes[p.index].color == 'white':
                self.nodes[p.index].p = node
                self.dfs_visit(self.nodes[p.index])
            p = p.next
        node.f = self.time
        self.parantheses += ')'
        node.color = 'black'

class Search:
    @staticmethod
    def dfs(graph):
        dfg = DepthFirstGraph(graph)
        dfg.dfs()
        return dfg

    @staticmethod
    def dfs_stack(graph):
        dfg = DepthFirstGraph(graph)
        dfg.dfs_stack()
        return dfg

if __name__ == '__main__':
    adjs = [[('a', 0), ('c', 1), ('b', 1)],
            [('b', 0), ('d', 1)],
            [('c', 0), ('b', 1)],
            [('d', 0), ('f', 1), ('c', 1)],
            [('e', 0), ('f', 1), ('d', 1)],
            [('f', 0), ('a', 1)]]
    graph = G.generate_adjacency(adjs)
    graph.print()
    print(' ----')
    r = Search.dfs(graph)
    print(r.parantheses)
    print(' ----')
    for t in r.traversal:
        print(t.info())
    print(' ----')
    r = Search.dfs_stack(graph)
    print(r.parantheses)
    print(' ----')
    for t in r.traversal:
        print(t.info())
