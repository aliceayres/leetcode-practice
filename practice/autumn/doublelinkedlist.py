'''
Double linked list
双链表
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkList:

    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def list_search(self,k):
        p = self.head.next
        while p != self.head:
            if p.data == k:
                return p
            p = p.next
        return None

    def list_head_insert(self,x):
        node = Node(x)
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        return

    def list_delete(self,x):
        p = self.head.next
        while p != self.head :
            if p.data == x:
                p.next.prev = p.prev
                p.prev.next = p.next
            p = p.next
        return

    def tolist(self):
        next = self.head.next
        list = []
        while next != self.head:
            list.append(next.data)
            next = next.next
        return list

if __name__ == '__main__':
    dll = DoubleLinkList()
    dll.list_head_insert(3)
    dll.list_head_insert(2)
    dll.list_head_insert(1)
    print(dll.tolist())
    print(dll.list_search(2))
    dll.list_delete(3)
    print(dll.tolist())

