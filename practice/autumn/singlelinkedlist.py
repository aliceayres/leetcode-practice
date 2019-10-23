'''
Linked list 普通单链表
10.2-7 n时间逆转
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node(None)

    def reverse(self):
        first = self.head.next
        if first is None:
            return
        p = first.next
        first.next = None
        while p is not None:
            node = p
            p = p.next  # this before
            self.list_head_insert_node(node)

    def list_search(self,k):
        p = self.head.next
        while p is not None:
            if p.data == k:
                return p
            p = p.next
        return None

    def list_delete_first(self):
        first = self.head.next
        if first is not None:
            self.head.next = first.next
        return first

    def list_head_insert_node(self,node):
        node.next = self.head.next
        self.head.next = node

    def list_head_insert(self,x):
        node = Node(x)
        self.list_head_insert_node(node)

    def list_tail_insert(self,x):
        node = Node(x)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node


    def list_delete(self,x):
        prev = self.head
        p = self.head.next
        while p is not None:
            if p.data == x:
                prev.next = p.next
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
    dll.list_head_insert(5)
    dll.list_head_insert(4)
    dll.list_head_insert(3)
    dll.list_head_insert(2)
    dll.list_head_insert(1)
    print(dll.tolist())
    print(dll.list_search(2))
    # dll.list_delete(3)
    dll.reverse()
    print(dll.tolist())

