'''
Disjoint-Set based Forest 不相交集合森林
21.3-4 print-set(x): add property children → o(A)
'''

class ForestNode:
    def __init__(self,data):
        self.data = data
        self.p = self
        self.r = 1
        self.children = []

class DisjointSet:
    @staticmethod
    def make_set(x):
        '''
        :param x: data
        :return: node
        '''
        node = ForestNode(x)
        return node

    @staticmethod
    def union(x,y):
        '''
        union by rank
        :param x: node
        :param y: node
        :return: node
        '''
        a = DisjointSet.find_set(x)
        b = DisjointSet.find_set(y)
        if a.r < b.r:
            a.p = b
            b.children.append(a)
            return b
        else:
            b.p = a
            a.children.append(b)
            if a.r == b.r:
                a.r += 1
            return a

    @staticmethod
    def find_set_two_path(x):
        '''
        path compression
        :param x: node
        :return: node
        '''
        if x.p != x:
            x.p.children.pop(x.p.children.index(x))
            pr = DisjointSet.find_set(x.p)
            x.p = pr # two-path method
            pr.children.append(x)
        return x.p # must be x.p not x

    @staticmethod
    def find_set(x):
        '''
        path compression
        :param x: node
        :return: node
        '''
        p = x
        while p.p != p:
            p = p.p
        c = x
        while c.p != c:
            pr = c.p
            pr.children.pop(pr.children.index(c))
            c.p = p
            p.children.append(c)
            c = pr
        return p

    @staticmethod
    def print_set(x):
        root = DisjointSet.find_set(x)
        DisjointSet.print_forest(root)

    @staticmethod
    def print_forest(x):
        print(x.data)
        for e in x.children:
            DisjointSet.print_forest(e)


if __name__ == '__main__':
    x = 'A'
    y = 'B'
    z = 'C'
    xn = DisjointSet.make_set(x)
    print(xn)
    yn = DisjointSet.make_set(y)
    xn = DisjointSet.union(xn, yn)
    DisjointSet.print_set(xn)
    xs = DisjointSet.find_set(xn)
    ys = DisjointSet.find_set(yn)
    print(xs, ys)
    zn = DisjointSet.make_set(z)
    xn = DisjointSet.union(xn, zn)
    xs = DisjointSet.find_set(xn)
    ys = DisjointSet.find_set(yn)
    zs = DisjointSet.find_set(zn)
    print(xs, zs, ys)
    DisjointSet.print_set(xn)