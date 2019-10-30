'''
Red-Black Tree 红黑树
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
    def __init__(self,array = None):
        self.array = array
        self.nil = Node(None,color='black')
        self.root = self.build_rbtree(array)

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

    def rb_insert(self,z):
        node = Node(z,color='red',left=self.nil,right=self.nil,parent=self.nil)
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
        self.rb_update_fixup(node)

    def rb_update_fixup(self,x):
        node = x
        while node != self.root and node.p.color == 'red':
            self.level_travelsal()
            grand = node.p.p
            if grand == self.nil:
                break
            if grand.left == node.p:
                uncle = grand.right
                if uncle != self.nil and uncle.color == 'red':
                    # case 1: uncle is red then: grand = red, parent & uncle = black, node = grand
                    grand.color = 'red'
                    uncle.color = 'black'
                    node.p.color = 'black'
                    node = grand
                else:
                    if node.p.right == node:
                        # case 2: different side then: rotate parent-node, node = original parent
                        # rotate-direction: right child then parent left rotate, original parent is new left child
                        self.left_rotation(node.p)
                        node = node.left
                    # cace 3: same side then: rotate grand-parent, grand = red, parent = black
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
        if node is None:
            return
        y = node.left
        if y is None:
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
        if y.right is not None:
            y.right.p = node
        y.right = node
        node.p = y

    def right_rotation_value(self,x):
        node = self.search(x)
        self.right_rotation(node)

    def left_rotation(self,node):
        if node is None:
            return
        y = node.right
        if y is None:
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
        if y.left is not None:
            y.left.p = node
        y.left = node
        node.p = y

    def left_rotation_value(self,x):
        node = self.search(x)
        self.left_rotation(node)

if __name__ == '__main__':
    array = [[7, 'black', 1,2], [3,'black',None,None], [18,'red',3,4], [10,'black',5,6], [22,'black',None,7], [8,'red',None,None], [11,'red',None,None], [26,'red',None,None]]
    rb = RBTree(array=array)
    rb.level_travelsal()
    rb.rb_insert(15)
    print('tree after rb insert 15:')
    rb.level_travelsal()
    rb.sorted_traversal()
