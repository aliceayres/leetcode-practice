'''
BST 二叉搜索树
'''

import random
class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        return

class BST:
    def __init__(self,num):
        self.root = None
        self.build(num)
        self.sorted = []
        self.dlr_cache = []

    def dlr_bst(self):
        self.dlr_cache = []
        self.dlr(self.root)
        return self.dlr_cache

    def dlr(self,p):
        if p is None:
            return
        self.dlr_cache.append(p.key)
        self.dlr(p.left)
        self.dlr(p.right)

    def sort_bst(self):
        self.sorted = []
        self.traversal(self.root)
        return self.sorted

    def traversal(self,p):
        if p is None:
            return
        self.traversal(p.left)
        self.sorted.append(p.key)
        self.traversal(p.right)


    def transplant(self,original,update): # transplant update replace to original
        if original.parent is None:
            self.root = update
        elif original.parent.left == original:
                original.parent.left = update
        else:
            original.parent.right = update
        if update is not None:
            update.parent = original.parent

    def delete(self,x): # delete is complex
        node = self.search(x)
        if node is None:
            return
        elif node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else: # 2 situation
            successor = self.successor(x)
            if successor != node.right:
                self.transplant(successor,successor.right)
                successor.right = node.right
                node.right.parent = successor.right
            self.transplant(node, successor)
            successor.left = node.left
            node.left.parent = successor

    def insert(self,x):
        p = self.root
        while True:
            if x >= p.key:
                if p.right is None:
                    p.right = Node(x, parent=p)
                    break
                else:
                    p = p.right

            if x < p.key:
                if p.left is None:
                    p.left = Node(x, parent=p)
                    break
                else:
                    p = p.left

    def build(self,num):
        if num is None or len(num) == 0:
            return None
        idx = random.randint(0,len(num)-1)
        self.exch(num,idx,0)
        root = Node(num[0])
        self.root = root
        for i in range(1,len(num)):
            idx = random.randint(i,len(num)-1)
            self.exch(num, idx, i)
            x = num[i]
            self.insert(x)

    def exch(self,num,i,j):
        t = num[i]
        num[i] = num[j]
        num[j] = t

    def search(self,x):
        p = self.root
        while p is not None:
            if p.key > x:
                p = p.left
            elif p.key < x:
                p = p.right
            else:
                return p
        return None

    def leftest(self,node):
        p = node
        while True:
            if p.left is None:
                return p
            p = p.left

    def predecessor(self,x):
        node = self.search(x)
        if node is None:
            return None
        parent = node.parent
        if node.left is not None:    # has left: rightest of left child
            return self.rightest(node.left)
        else:
            child = node
            p = parent
            while p is not None and p.left == child: # nearest right root
                child = p
                p = p.parent
            return p

    def successor(self,x):
        node = self.search(x)
        if node is None:
            return None
        parent = node.parent
        if node.right is not None:  # has right: leftest of right child
            return self.leftest(node.right)
        else:
            child = node
            p = parent
            while p is not None and p.right == child:   # nearest left root
                child = p
                p = p.parent
            return p

    def rightest(self,node):
        p = node
        while True:
            if p.right is None:
                return p
            p = p.right

    def min(self):
        return self.leftest(self.root)

    def max(self):
        return self.rightest(self.root)

if __name__ == '__main__':
    num = [2,1,8,3,20,5,15,9,7,32]
    print(num)
    bst = BST(num)
    print('sorted',bst.sort_bst(),'dlr',bst.dlr_bst())
    print(bst.search(15))
    print(bst.search(25))
    print(bst.min().key)
    print(bst.max().key)
    print('predecessor:')
    for e in bst.sort_bst():
        node = bst.predecessor(e)
        if node is None:
            print(None)
        else:
            print(node.key)
    print('successor:')
    for e in bst.sort_bst():
        node = bst.successor(e)
        if node is None:
            print(None)
        else:
            print(node.key)
    bst.delete(15)
    print('sorted',bst.sort_bst(),'dlr',bst.dlr_bst())