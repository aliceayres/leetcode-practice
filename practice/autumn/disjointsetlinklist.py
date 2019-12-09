'''
Disjoint-Set based Linked List 不相交集合的链表表示
'''

class LinkedListSet:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        print(self.head.data,self.tail.data,self.length)

class Node:
    def __init__(self,data):
        self.set = None
        self.data = data
        self.next = None

class DisjointSet:
    @staticmethod
    def make_set(x):
        '''
        :param x: data
        :return: node
        '''
        node = Node(x)
        djset = LinkedListSet()
        if djset.head is not None:
            djset.tail.next = node
            djset.tail = node
        else:
            djset.head = node
            djset.tail = node
        djset.length += 1
        node.set = djset
        return node

    @staticmethod
    def union(x,y):
        '''
        :param x: node
        :param y: node
        :return: node
        '''
        xset = x.set
        yset = y.set
        if yset.length > xset.length: # weight-union : longer union shorter (x.length >= y.length)
            xset = y.set
            yset = x.set
        p = yset.head
        while p is not None:
            p.set = xset
            p = p.next
        xset.tail.next = yset.head
        xset.tail = yset.tail
        xset.length += yset.length
        return x

    @staticmethod
    def union_off_tail(x,y):
        '''

        :param x: node
        :param y: node
        :return: node
        '''
        xset = x.set
        yset = y.set
        if yset.length > xset.length:  # weight-union : longer union shorter (x.length >= y.length)
            xset = y.set
            yset = x.set
        p = yset.head
        pre = None
        while p is not None:
            p.set = xset
            pre = p
            p = p.next
        pre.next = xset.head
        xset.head = yset.head
        xset.length += yset.length
        return x

    @staticmethod
    def find_set(x):
        '''
        :param x: node
        :return: set
        '''
        return x.set

if __name__ == '__main__':
    x = 'A'
    y = 'B'
    z = 'C'
    xn = DisjointSet.make_set(x)
    print(xn.set)
    yn = DisjointSet.make_set(y)
    xn = DisjointSet.union(xn, yn)
    # xn = DisjointSet.union_off_tail(xn,yn)
    xs = DisjointSet.find_set(xn)
    ys = DisjointSet.find_set(yn)
    print(xs, ys)
    zn = DisjointSet.make_set(z)
    xn = DisjointSet.union(xn, zn)
    # xn = DisjointSet.union_off_tail(xn,zn)
    xs = DisjointSet.find_set(xn)
    ys = DisjointSet.find_set(yn)
    zs = DisjointSet.find_set(zn)
    print(xs, zs, ys)