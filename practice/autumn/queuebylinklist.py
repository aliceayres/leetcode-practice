'''
单链表实现队列 10.2-3
'''

from practice.autumn import linkedlist as li

class QueueL:
    def __init__(self):
        self.linklist = li.LinkedList()

    def print(self):
        print(self.linklist.tolist())

    def enqueue(self,x):
        self.linklist.list_tail_insert(x)
        return

    def dequeue(self):
        top = self.linklist.list_delete_first()
        if top is None:
            raise Exception('stack underflow')
        return top.data

if __name__ == '__main__':
    q = QueueL()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    q.print()