'''
合并K个有序链表 nlgk
最小堆K路归并
'''
from practice.autumn import heapmin as hp

class LinkNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def solute(self,headers):
        result = LinkNode(-1,None)
        head = result
        nodes = []
        for header in headers:
            node =  hp.Node(header.next,header.next.data) # current index, data
            nodes.append(node)
        heap = hp.Heap(nodes)
        while len(heap.heap) > 0:
            min_lnode = heap.heap[0].data
            head.next = min_lnode
            head = min_lnode
            heap.heap_delete(0)
            next_lnode = min_lnode.next
            if next_lnode is not None:
                next_node = hp.Node(next_lnode,next_lnode.data)
                heap.heap_insert(next_node)
        return result

    def tolink(self,num):
        header = LinkNode("head")
        pre = header
        for e in num:
            node = LinkNode(e)
            pre.next = node
            pre = node
        return header

    def tolist(self,header):
        next = header.next
        list = []
        while next is not None:
            list.append(next.data)
            next = next.next
        return list

if __name__ == '__main__':
    slt = Solution()
    num1 = [2,6,15,22]
    num2 = [3,5,18,23]
    num3 = [12,26]
    header1 = slt.tolink(num1)
    header2 = slt.tolink(num2)
    header3 = slt.tolink(num3)
    print(slt.tolist(header1))
    result = slt.solute([header1,header2,header3])
    print(result)
    print(slt.tolist(result))
