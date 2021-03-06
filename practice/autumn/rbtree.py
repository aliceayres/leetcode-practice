'''
Red-Black Tree 红黑树
build red-black tree 13.3-2
'''

class Node:
    def __init__(self,key,left=None,right=None,parent=None,color='red'):
        self.key = key
        self.p = parent
        self.left = left
        self.right = right
        self.color = color
        return

class RBTree:
    def __init__(self):
        self.root = None
        self.nil = Node(None,color='black')

    def build_node(self,array, index):
        info = array[index]
        node = Node(info[0], color=info[1])
        if info[2] is not None:
            left = self.build_node(array, info[2])
            node.left = left
            left.p = node
        else:
            node.left = self.nil
        if info[3] is not None:
            right = self.build_node(array, info[3])
            node.right = right
            right.p = node
        else:
            node.right = self.nil
        node.p = self.nil
        return node

    def build_rbtree(self,array):
        return self.build_node(array,0)

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
                print('(',e.key,e.color,prkey,')',end=' ')
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

    def traversal(self,p,sorted):
        if p == self.nil:
            return
        self.traversal(p.left,sorted)
        sorted.append(p.key)
        self.traversal(p.right,sorted)

    def build(self,num):
        for e in num:
            self.rb_insert(e)

    def rb_transplant(self, u, v):  # transplant v replace to u
        if u.p == self.nil:
            self.root = v
        elif u.p.left == u:
            u.p.left = v
        else:
            u.p.right = v
        if v != self.nil:
            v.p = u.p

    def rb_delete(self,z):
        node = self.search(z)
        if node == self.nil:
            return
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
            # x.color = yoc
        else:
            y = self.successor(node)
            yoc = y.color
            x = y.right
            if y != node.right:
                self.rb_transplant(y,x)
                y.right = node.right
                node.right.p = y
            self.rb_transplant(node, y)
            y.left = node.left
            node.left.p = y
            y.color = node.color
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
            elif x > p.key :
                p = p.right
            else:
                return p
        return self.nil

    def rb_insert(self,z):
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

    def right_rotation(self,node):
        if node == self.nil:
            return
        y = node.left
        if y == self.nil:
            return
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
    rbt.sorted_traversal()
    '''
    array = [[7, 'black', 1,2], [3,'black',None,None], [18,'red',3,4], [10,'black',5,6], [22,'black',None,7], [8,'red',None,None], [11,'red',None,None], [26,'red',None,None]]
    rb = RBTree()
    rb.root = rb.build_rbtree(array)
    rb.level_travelsal()
    rb.rb_insert(15)
    rb.level_travelsal()
    rb.rb_delete(18)
    rb.level_travelsal()
    '''


