'''
Skiplist 跳表(理想不必要)
Skiplist limit: head & tail must be in Level highest & best level = lgn
'''
import random
import math

class Node:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None
        self.up = None
        self.down = None

def randomHalf():
    return random.randint(1, 100) > 50

# Skiplist 1 : head & tail must be in Level highest & best level = lgn
class Skiplist:
    def __init__(self):
        self.header = None
        self.base = None
        self.count = 0
        self.level = 0

    def bestlevel(self):
        return math.floor(math.log(self.count,2))+1

    def insert(self,x):
        print('insert:', x)
        prev = self.search_insert(x)
        if self.header is None: # skip list is empty, to initialize
            node = Node(x)
            self.header = node
            self.base = node
            self.count += 1
            self.level = self.bestlevel()
            return
        if prev is None: # insert head
            original = self.base.key
            self.replace_up_level(self.base,x)
            self.traversal()
            self.insert(original)
            return
        if prev.next is None: # insert tail
            original = prev.key
            self.replace_up_level(prev,x)
            self.traversal()
            self.insert(original)
            return
        node = Node(x)
        self.count += 1
        self.link(prev,node)
        up_level = self.bestlevel()
        cnt = 1
        while randomHalf() is True and cnt <= up_level:
            print(cnt,self.level,up_level)
            p = prev
            if cnt == up_level and up_level > self.level:  # level will up
                h = Node(self.header.key)
                h.down = self.header
                self.header.up = h
                tail = self.header
                while tail.next is not None:
                    tail = tail.next
                t = Node(tail.key)
                t.down = tail
                tail.up = t
                h.next = t
                t.prev = h
                nd = Node(x)
                nd.down = node
                node.up = nd
                self.link(h,nd)
                self.header = h
                self.level += 1
            else:
                while p is not None and p.up is None:
                    p = p.prev
                up_node = Node(x)
                up_node.down = node
                node.up = up_node
                if p is not None:
                    self.link(p.up,up_node)
                node = up_node
                prev = up_node.prev
            cnt += 1
        return

    def link(self,prev,node):
        node.next = prev.next
        if prev.next is not None:
            prev.next.prev = node
        prev.next = node
        node.prev = prev
        return

    def replace_up_level(self,original,x):
        p = original
        while p is not None:
            p.key = x
            p = p.up
        return

    def delete(self,x):
        return

    def search_insert(self,x):
        p = self.header
        if p is None:
            return None
        if x < p.key:
            return None
        while p is not None:
            if x > p.key:
                pr = p
                p = p.next
            elif x < p.key:
                pr = p.prev
                p = p.prev.down
        while pr.down is not None:
            pr = pr.down
        return pr

    def search(self,x):
        p = self.header
        if self.header is None:
            return None
        if x < p.key:
            return None
        while p is not None:
            if x > p.key:
                p = p.next
            elif x < p.key:
                p = p.prev.down
            else:
                break
        while p is not None and p.down is not None:
            p = p.down
        return p

    def build(self,num):
        self.base = Node(num[0])
        prev = self.base
        for i in range(1,len(num)):
            node = Node(num[i])
            prev.next = node
            node.prev = prev
            prev = node
        begin = self.base
        cnt = len(num)
        while cnt > 2:
            p = begin
            pr = None
            cnt = 0
            while p is not None:
                if p.next is not None and p.next.key == num[-1]:
                    p = p.next
                up = Node(p.key)
                cnt += 1
                if pr is None:
                    begin = up
                up.prev = pr
                if pr is not None:
                    pr.next = up
                p.up = up
                up.down = p
                pr = up
                if p.next is not None:
                    p = p.next.next
                else:
                    p = None
        self.header = begin
        self.count = len(num)
        return

    def traversal(self):
        p = self.header
        i = 1
        while p is not None:
            print('level %d = '% i, end=' ')
            node = p
            while node is not None:
                print(node.key,end=' ')
                node = node.next
            print()
            p = p.down
            i += 1

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
