'''
Skiplist 跳表（高概率 lgn）
head & tail not must be in Level highest & best level = lgn
but head must be in level highest (real skiplist) let head key sys.min
todo : * restruct Node —— up-down point in a array, level = len(array)
'''
import random
import sys

class Node:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None
        self.up = None
        self.down = None

def randomHalf():
    return random.randint(1, 100) > 50

# Skiplist 2 : head must be in level highest (real skiplist)
class Skiplist:
    def __init__(self):
        self.header = Node(-sys.maxsize)

    def insert(self,x):
        prev = self.search_insert(x)
        p = Node(x)
        p.next = prev.next
        if prev.next is not None:
            prev.next.prev = p
        prev.next = p
        p.prev = prev
        while randomHalf() is True:
            up = Node(x)
            up.down = p
            p.up = up
            down_prev = p.prev
            while down_prev.up is None:
                if down_prev.key == self.header.key:
                    break
                down_prev = down_prev.prev
            if down_prev.key == self.header.key and down_prev.up is None:
                up_prev = Node(self.header.key)
                up_prev.down = self.header
                self.header.up = up_prev
                self.header = up_prev
            else:
                up_prev = down_prev.up
            up.next = up_prev.next
            if up_prev.next is not None:
                up_prev.next.prev = up
            up_prev.next = up
            up.prev = up_prev
            p = up
        return

    def search(self,x):
        p = self.header
        while p is not None:
            if x > p.key:
                if p.next is not None:
                    p = p.next
                else:
                    p = p.down
            elif x < p.key:
                p = p.prev.down
            else:
                while p.down is not None:
                    p = p.down
                return p
        return p

    def search_insert(self,x):
        p = self.header
        prev = None
        while p is not None:
            if x <= p.key:
                if p.prev is not None and p.prev.down is not None:
                    p = p.prev.down
                    prev = p
                elif p.prev is None:
                    prev = p
                    p = None
                else:
                    prev = p.prev
                    p = None
            elif x > p.key:
                if p.down is None:
                    prev = p
                    p = p.next
                else:
                    prev = p
                    p = p.down
        while prev.down is not None:
            prev = prev.down
        return prev

    def delete(self,x):
        return

    def build(self,num):
        for e in num:
            self.insert(e)
        return

    def traversal(self):
        p = self.header
        i = 1
        while p is not None:
            print('level %d = ' % i, end=' ')
            node = p
            while node is not None:
                print(node.key, end=' ')
                node = node.next
            print()
            p = p.down
            i += 1
        return

if __name__ == '__main__':
    sl = Skiplist()
    sl.traversal()
    num = [14,23,34,80,92,100]
    sl.build(num)
    sl.traversal()
    add = [42,50,59,66,16,49,72,12,180,78]
    for e in add:
        sl.insert(e)
    sl.traversal()
    node = sl.search(42) # 42 12 99 190
    if node is not None:
        print(node.key,node.down)
    node = sl.search(12)  # 42 12 99 190
    if node is not None:
        print(node.key, node.down)
    node = sl.search(99)  # 42 12 99 190
    if node is not None:
        print(node.key, node.down)
    node = sl.search(100)  # 42 12 99 190
    if node is not None:
        print(node.key, node.down)
    node = sl.search_insert(198)  # 12 198
    if node is not None:
        print(node.key, node.down)
