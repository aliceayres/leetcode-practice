'''
'''


class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        return

class BST:
    def __init__(self,num):
        self.root = self.build(num)
        self.sorted = []

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

    def build(self,num):
        if num is None or len(num) == 0:
            return None
        root = Node(num[0])
        for i in range(1,len(num)):
            p = root
            while True:
                if num[i] >= p.key:
                    if p.right is None:
                        p.right = Node(num[i],parent=p)
                        break
                    else:
                        p = p.right

                if num[i] < p.key:
                    if p.left is None:
                        p.left = Node(num[i],parent=p)
                        break
                    else:
                        p = p.left
        return root

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
    st = bst.sort_bst()
    print('sorted',st)
    print(bst.search(15))
    print(bst.search(25))
    print(bst.min().key)
    print(bst.max().key)
    print('predecessor:')
    for e in st:
        node = bst.predecessor(e)
        if node is None:
            print(None)
        else:
            print(node.key)
    print('successor:')
    for e in st:
        node = bst.successor(e)
        if node is None:
            print(None)
        else:
            print(node.key)
