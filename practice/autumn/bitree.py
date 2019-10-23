'''
BiTree 二叉树数组存储
'''
class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        return

    def __repr__(self):
        return format("(key=%s,parent=%s,left=%s,right=%s)" % (self.key,self.parent,self.left,self.right))

class BiTree:
    def __init__(self,dictionary,root):
        self.dictionary = dictionary
        self.root = root

    def recursion_traversal(self,p,result):
        # result.append(p.key)
        if p.left is not None:
            self.recursion_traversal(self.dictionary[p.left],result)
        # result.append(p.key)
        if p.right is not None:
            self.recursion_traversal(self.dictionary[p.right],result)
        result.append(p.key)
        return result

    def lrd(self):
        result = []
        p = self.root
        stack = [None]
        while p is not None:
            if p.left is not None:
                stack.append(p)
                p = self.dictionary[p.left]
            else:
                if p.right is None:
                    result.append(p.key)
                    pr = stack[-1]
                    # search for next right tree
                    while (pr is not None and self.dictionary[pr.left] == p and pr.right is None) or (pr is not None and self.dictionary[pr.right] == p):
                        result.append(pr.key)
                        p = stack.pop(-1)
                        pr = stack[-1]
                    if pr is not None and pr.right is not None and self.dictionary[pr.right] != p:
                        p = self.dictionary[pr.right]
                    else:
                        break
                else:
                    p = self.dictionary[p.right]
        return result

    def ldr(self):
        result = []
        p = self.root
        stack = [None]
        while p is not None:  # p is current deal with
            if p.left is not None:  # if left not None: push p and p = left
                stack.append(p)
                p = self.dictionary[p.left]
            else:
                while p is not None and p.right is None:  # otherwise: left done, print p and pop stack
                    result.append(p.key)    # while stack right None print
                    p = stack.pop(-1)
                if p is None:
                    break
                result.append(p.key)   # if right not None: print p (d) before ,  self = right
                p = self.dictionary[p.right]
        return result

    def dlr(self):
        result = []
        p = self.root
        stack = [None]
        while p is not None:
            result.append(p.key)   # print self (d)
            if p.right is not None:
                stack.append(self.dictionary[p.right])  # push right
            if p.left is not None:
                stack.append(self.dictionary[p.left])   # push left
            p = stack.pop(-1)  # pop stack
        return result

def tobitree(array,ridx):
    p = (ridx,None)
    stack = [None]
    root = None
    dic = [None for i in range(len(array))]
    while p is not None:
        i = p[0]
        parent = p[1]
        if i < len(array):
            data = array[i]
            node = Node(data[0],data[1],data[2],parent)
            dic[i] = node
            if root is None:
                root = node
            if data[2] is not None:
                stack.append((data[2],i))
            if data[1] is not None:
                stack.append((data[1],i))
        p = stack.pop(-1)
    tree = BiTree(dic,root)
    return tree

if __name__ == '__main__':
    ridx = 5
    array = [[12,7,3],[15,8,None],[4,10,None],[10,5,9],[2,None,None],[18,1,4],[7,None,None],[14,6,2],[21,None,None],[5,None,None]]
    for e in array:
        if e[1] is not None:
            e[1] -= 1
        if e[2] is not None:
            e[2] -= 1
    print(array)
    tree = tobitree(array,ridx)
    print(tree.root)
    for i in range(len(tree.dictionary)):
        print(i,tree.dictionary[i])
    print("dlr:",tree.dlr())
    print("ldr",tree.ldr())
    print("lrd", tree.lrd())
    print(tree.recursion_traversal(tree.root,[]))