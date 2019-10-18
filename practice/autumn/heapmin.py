'''
最小堆
'''
import sys
class Node:
    def __init__(self,data,key):
        self.data = data
        self.key = key

    def __str__(self):
        return format('data=%s,key=%s' % (str(self.data),str(self.key)))

class Heap:
    def __init__(self,nodes):
        self.heap = nodes
        self.build_min_heap()

    def print_heap(self):
        for e in self.heap:
            print(e)


    def build_min_heap(self):
        i = self.leafbegin(len(self.heap)) - 1
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def heap_insert(self,node):
        k = node.key
        node.key = sys.maxsize
        self.heap.append(node)
        self.decrease_key(len(self.heap) - 1, k)

    def decrease_key(self,idx,k):
        parent = self.parent(idx)
        i = idx
        self.heap[idx].key = k
        while parent >= 0 and self.heap[parent].key > k:
            self.exch(self.heap,i,parent)
            i = parent
            parent = self.parent(parent)
        return

    def heap_delete(self,i):
        deleted = self.heap[i]
        self.heap[i] = self.heap[-1]
        self.heap.pop(-1)
        self.min_heapify(i)
        return deleted

    def extract_min(self):
        min = self.heap[0]
        self.heap_delete(0)
        return min

    def min_heapify(self,i):
        length = len(self.heap)
        smallest = i
        l = self.left(i)
        r = self.right(i)
        if l < length and self.heap[l].key <= self.heap[i].key:
            smallest = l
        if r < length and self.heap[r].key <= self.heap[smallest].key:  # this compare large and r!
            smallest = r
        if smallest != i:
            self.exch(self.heap,smallest,i)
            self.min_heapify(smallest)

    def exch(self, num, a, b):
        t = num[a]
        num[a] = num[b]
        num[b] = t

    def parent(self,i):
        # return (i-1)>>1
        return (i-1)//2

    def left(self,i):
        # return (i<<1)+1
        return 2*i+1

    def right(self,i):
        # return (i+1)<<1
        return 2*i+2

    def leafbegin(self,n):
        return n//2

if __name__ == '__main__':
    num = [("a", 7), ("b", 9), ("c", 11), ("d", 2), ("e", 6), ("f", 5), ("g", 8), ("h", 3), ("i", 4), ("j", 1)]
    nodes = []
    for e in num:
        node = Node(e[0], e[1])
        nodes.append(node)
    h = Heap(nodes)
    h.print_heap()
    h.heap_delete(0)
    print()
    h.print_heap()
    h.heap_insert(Node('x',0))
    print()
    h.print_heap()