'''
单链表实现栈 10.2-2
'''
from practice.autumn import linkedlist as li

class StackL:
    def __init__(self):
        self.linklist = li.LinkedList()

    def print(self):
        print(self.linklist.tolist())

    def push(self,x):
        self.linklist.list_head_insert(x)
        return

    def pop(self):
        top = self.linklist.list_delete_first()
        if top is None:
            raise Exception('stack underflow')
        return top.data

if __name__ == '__main__':
    s = StackL()
    s.push(3)
    s.push(1)
    print(s.pop())
    s.push(2)
    print(s.pop())
    print(s.pop())
