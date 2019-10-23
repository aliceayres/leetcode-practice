'''
Linked list 单链表(记录尾节点）
尾插法o(1)
10.2-6 o(1)时间Union两个不想交的集合 利用链表
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def list_search(self,k):
        p = self.head.next
        while p is not None:
            if p.data == k:
                return p
            p = p.next
        return None

    def list_delete_first(self):
        first = self.head.next
        if first == self.tail:
            self.tail = self.head
        if first is not None:
            self.head.next = first.next
        return first

    def list_head_insert(self,x):
        node = Node(x)
        if self.tail == self.head:
            self.tail = node
        node.next = self.head.next
        self.head.next = node
        return

    def list_tail_insert(self,x):
        node = Node(x)
        self.tail.next = node
        self.tail = node
        # p = self.head
        # while p.next is not None:
        #     p = p.next
        # p.next = node


    def list_delete(self,x):
        prev = self.head
        p = self.head.next
        while p is not None:
            if p.data == x:
                prev.next = p.next
                if p == self.tail:
                    self.tail = prev
            prev = p
            p = p.next
        return

    def tolist(self):
        p = self.head.next
        list = []
        while p is not None:
            list.append(p.data)
            p = p.next
        return list

if __name__ == '__main__':
    dll = LinkedList()
    dll.list_head_insert(3)
    dll.list_head_insert(2)
    dll.list_head_insert(1)
    print(dll.tolist())
    print(dll.list_search(2))
    dll.list_delete(3)
    print(dll.tolist())

