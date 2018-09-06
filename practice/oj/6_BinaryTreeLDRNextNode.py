'''
6. 二叉树的下一个结点
题目描述：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def toString(self):
        str = "value=[%d]" % self.value
        if self.left:
            str += " left.value=[%d]" % self.left.value
        if self.right:
            str += " right.value=[%d]" % self.right.value
        if self.parent:
            str += " parent.value=[%d]" % self.parent.value
        return str


class Solution:
    def getInOrderNextNode(self, node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            parent = node.parent
            while parent and parent.left != node:
                node = parent
                parent = node.parent
            return parent

    def traversionInInOrder(self,root): # LDR
        order = []
        stack = []
        node = root
        while node or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop(-1)
                order.append(node.value)
                node = node.right
        return order

    def rebuildBinaryTree(self, preorder,inorder,parent):
        value = preorder[0]
        root = TreeNode(value)
        root.parent = parent
        root_idx = inorder.index(value)
        if root_idx != 0: # left exist
            left_in = [inorder[0]]
            left_pre = [preorder[1]]
            if root_idx-1 > 0:
                left_in = inorder[0:root_idx]
                left_pre = preorder[1:1+root_idx]
            root.left = self.rebuildBinaryTree(left_pre,left_in,root)
        if root_idx != len(inorder)-1: # right exist
            right_in = [inorder[-1]]
            right_pre = [preorder[-1]]
            if root_idx < len(inorder)-2:
                right_in = inorder[root_idx+1:]
                right_pre = preorder[root_idx+1:]
            root.right = self.rebuildBinaryTree(right_pre,right_in,root)
        return root

slt = Solution()
preorder = [1,2,4,5,7,8,3,6,9,10,11]
inorder = [4,2,5,8,7,1,6,10,9,11,3]
root = slt.rebuildBinaryTree(preorder,inorder,None)
print(inorder)
print(slt.traversionInInOrder(root))
print(root.toString())
node1 = slt.getInOrderNextNode(root)
print(node1.toString())
print(root.left.right.right.toString())
node2 = slt.getInOrderNextNode(root.left.right.right)
print(node2.toString())
