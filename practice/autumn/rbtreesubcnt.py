'''
Red-Black Tree 红黑树
14 Order static tree based on red-black tree 顺序统计树
os_select 查找具有给定秩的元素（非递归） 14.1-3
os_rank 确定一个元素的秩
'''

class Node:
    def __init__(self,key,left=None,right=None,parent=None,color='red',size = 1):
        self.key = key
        self.p = parent
        self.left = left
        self.right = right
        self.color = color
        self.size = size
        return

class RBTree:
    def __init__(self):
        self.root = None
        self.nil = Node(None,color='black',size=0)

    def os_select(self,i):  # return ith element in rbtree
        if i > self.root.size or i < 1:
            return None
        p = self.root
        k = i
        while p != self.nil:
            sub = p.left.size + 1
            if sub == k:
                return p
            if sub > k:
                p = p.left
            else:
                p = p.right
                k = k - sub
        return None

    def os_rank(self,x): # return x's rank in rbtree
        node = self.search(x)
        p = node
        rank = p.left.size + 1
        while p != self.root:
            if p.p.right == p:
                rank += p.p.left.size + 1
            p = p.p
        return rank

    def os_rank_at_search(self,x): # return x's rank in rbtree at search
        tp = self.search_rank(x)
        return tp[1]

    def level_travelsal(self):
        print('---- level travelsal ----')
        p = self.root
        level = [self.nil,p]
        while len(level) != 1:
            for i in range(1,len(level)):
                e = level[i]
                prkey = None
                if e.p is not None:
                    prkey = e.p.key
                print('(',e.key,e.color,prkey,e.size,')',end=' ')
            print()
            p = level.pop(-1)
            stack = [self.nil]
            while p != self.nil:
                if p.right != self.nil:
                    stack.insert(1,p.right)
                if p.left != self.nil:
                    stack.insert(1,p.left)
                p = level.pop(-1)
            level = stack
        return

    def sorted_traversal(self):
        print('---- sorted travelsal ----')
        sorted = []
        self.traversal(self.root,sorted)
        print(sorted)
        return sorted

    def traversal(self,p,sorted):
        if p == self.nil:
            return
        self.traversal(p.left,sorted)
        sorted.append(p.key)
        self.traversal(p.right,sorted)

    def build(self,num):
        for e in num:
            self.rb_insert(e)
            # self.level_travelsal()

    def rb_transplant(self, u, v):  # transplant v replace to u, p.size = p - u + v
        if u.p == self.nil:
            self.root = v
        elif u.p.left == u:
            u.p.left = v
        else:
            u.p.right = v
        if v != self.nil:
            v.p = u.p

    def rb_delete(self,z): # node=delete
        node = self.search(z)
        if node == self.nil:
            return
        pr = node.p
        while pr != self.nil:
            pr.size -= 1
            pr = pr.p
        ons = node.size
        y = node
        yoc = y.color
        x = node.left
        if node.left == self.nil or node.right == self.nil:
            if node.left == self.nil:
                x = node.right
            if node.p == self.nil:
                self.root = x
            elif node.p.left == node:
                node.p.left = x
            else:
                node.p.right = x
            x.p = node.p
            x.color = yoc
        else:
            y = self.successor(node)
            yoc = y.color
            x = y.right
            if y != node.right:
                self.rb_transplant(y,x)
                y.right = node.right
                node.right.p = y
                node.right.size -= 1
            self.rb_transplant(node, y)
            y.left = node.left
            node.left.p = y
            y.color = node.color
            y.size = ons - 1
        if yoc == 'black':
            self.rb_delete_fixup(x)  # x.color = black2 or red-black : x.color + black
        self.root.p = self.nil
        self.root.color = 'black'

    def rb_delete_fixup(self,node):
        x = node
        # must be: x.p !== self.nil
        while x != self.root and x.color == 'black':
            if x.p.left == x:
                w = x.p.right
                if w.color == 'red':  # must be: w !== self.nil
                    w.color = 'black'
                    x.p.color = 'red'
                    self.left_rotation(x.p)
                else:
                    if w.left.color == 'black' and w.right.color == 'black':
                        w.color = 'red'
                        x = x.p
                    else:
                        if w.left.color == 'red' and w.right.color == 'black':
                            w.color = 'red'
                            w.left.color = 'black'
                            self.right_rotation(w)
                        w.color = x.p.color
                        x.p.color = 'black'
                        w.right.color = 'black'
                        self.left_rotation(x.p)
                        x = self.root
            else:
                # swap
                w = x.p.left
                if w.color == 'red':  # must be: w !== self.nil
                    w.color = 'black'
                    x.p.color = 'red'
                    self.right_rotation(x.p)
                else:
                    if w.left.color == 'black' and w.right.color == 'black':
                        w.color = 'red'
                        x = x.p
                    else:
                        if w.right.color == 'red' and w.left.color == 'black':
                            w.color = 'red'
                            w.right.color = 'black'
                            self.left_rotation(w)
                        w.color = x.p.color
                        x.p.color = 'black'
                        w.left.color = 'black'
                        self.right_rotation(x.p)
                        x = self.root
        x.color = 'black'

    def leftest(self,node):
        p = node
        while True:
            if p.left == self.nil:
                return p
            p = p.left

    def successor(self,node):
        if node == self.nil:
            return self.nil
        parent = node.p
        if node.right != self.nil:  # has right: leftest of right child
            return self.leftest(node.right)
        else:
            child = node
            p = parent
            while p != self.nil and p.right == child:   # nearest left root
                child = p
                p = p.p
            return p

    def search(self,x):
        p = self.root
        while p != self.nil:
            if x < p.key:
                p = p.left
            elif x > p.key:
                p = p.right
            else:
                return p
        return self.nil

    def search_rank(self,x):
        p = self.root
        rank = 0
        while p != self.nil:
            if x < p.key:
                p = p.left
            elif x > p.key:
                rank += p.left.size + 1
                p = p.right
            else:
                rank += p.left.size + 1
                return p,rank
        return self.nil,0

    def rb_insert(self,z): # node=insert leaf, y=parent
        node = Node(z,color='red',left=self.nil,right=self.nil,parent=self.nil)
        if self.root is None:
            self.root = self.nil
        x = self.root
        y = self.nil
        while x != self.nil:
            y = x
            if node.key <= y.key:
                x = y.left
            else:
                x = y.right
        if y == self.nil:
            self.root = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
        node.p = y
        pr = y
        while pr != self.nil:
            pr.size += 1
            pr = pr.p
        self.rb_insert_fixup(node)

    def rb_insert_fixup(self,po):
        node = po
        # to let the violation go up the tree
        while node != self.root and node.p.color == 'red':
            # self.level_travelsal()
            grand = node.p.p
            if grand == self.nil:
                break
            if grand.left == node.p:
                uncle = grand.right
                if uncle != self.nil and uncle.color == 'red':
                    # case 1: uncle is red then: grand = red, parent & uncle = black, node = grand
                    # this cause: the violation go up the tree 2 level, while will continue
                    # if go up to root, will end
                    grand.color = 'red'
                    uncle.color = 'black'
                    node.p.color = 'black'
                    node = grand
                else:
                    if node.p.right == node:
                        # case 2: different side then: rotate parent-node, node = original parent
                        # rotate-direction: right child then parent left rotate, original parent is new left child
                        # this cause: to case 3
                        self.left_rotation(node.p)
                        node = node.left
                    # cace 3: same side then: rotate grand-parent, grand = red, parent = black
                    # this cause: end
                    self.right_rotation(grand)
                    grand.color = 'red'
                    node.p.color = 'black'
            else:
                # the other direction: swap all the right and left
                uncle = grand.left
                if uncle != self.nil and uncle.color == 'red':
                    # case 1: uncle is red then: grand = red, parent & uncle = black, node = grand
                    grand.color = 'red'
                    uncle.color = 'black'
                    node.p.color = 'black'
                    node = grand
                else:
                    if node.p.left == node:
                        # case 2: different side then: rotate parent-node, node = original parent
                        # rotate-direction: left child then parent right rotate, original parent is new right child
                        self.right_rotation(node.p)
                        node = node.right
                    # cace 3: same side then: rotate grand-parent, grand = red, parent = black
                    self.left_rotation(grand)
                    grand.color = 'red'
                    node.p.color = 'black'
        self.root.color = 'black'
        self.root.p = self.nil
        return

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

    def right_rotation(self,node):
        if node == self.nil:
            return
        y = node.left
        if y == self.nil:
            return
        ons = node.size
        node.size = node.size - y.size + y.right.size
        y.size = ons
        print(y.key,y.size,node.key,node.size)
        if node.p == self.nil:
            self.root = y
        else:
            y.p = node.p
            if node.p.left == node:
                node.p.left = y
            else:
                node.p.right = y
        node.left = y.right
        if y.right != self.nil:
            y.right.p = node
        y.right = node
        node.p = y

    def left_rotation(self,node):
        if node == self.nil:
            return
        y = node.right
        if y == self.nil:
            return
        ons = node.size
        node.size = node.size - y.size + y.left.size
        y.size = ons
        print(y.key, y.size, node.key, node.size)
        if node.p == self.nil:
            self.root = y
        else:
            y.p = node.p
            if node.p.left == node:
                node.p.left = y
            else:
                node.p.right = y
        node.right = y.left
        if y.left != self.nil:
            y.left.p = node
        y.left = node
        node.p = y

if __name__ == '__main__':
    num = [23, 6, 16, 41, 38, 31, 12, 19, 8, 2, 56, 7, 34, 100]
    rbt = RBTree()
    rbt.build(num)
    rbt.level_travelsal()
    rbt.rb_delete(38)
    rbt.level_travelsal()
    st = rbt.sorted_traversal()
    for i in range(15):
        e = rbt.os_select(i)
        if e is None:
            print('*',end=' ')
        else:
            print(e.key,end=' ')
    print()
    for e in st:
        print(rbt.os_rank(e),end=' ')
    print()
    for e in st:
        print(rbt.os_rank_at_search(e), end=' ')


