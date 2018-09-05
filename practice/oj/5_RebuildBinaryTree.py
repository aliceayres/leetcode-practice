'''
5. 重建二叉树
题目描述：
根据二叉树的前序遍历和中序遍历的结果，重建出该二叉树。假设输入的前序遍历
和中序遍历的结果中都不含重复的数字。
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def traversingInPreorder(self,root): # DLR
        order = []
        stack = []
        node = root
        while node is not None:
            order.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                node = node.left
            else:
                if len(stack) != 0:
                    node = stack.pop(-1)
                else:
                    node = None
        return order

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

    def rebuildBinaryTree(self, preorder,inorder):
        value = preorder[0]
        root = TreeNode(value)
        root_idx = inorder.index(value)
        if root_idx != 0: # left exist
            left_in = [inorder[0]]
            left_pre = [preorder[1]]
            if root_idx-1 > 0:
                left_in = inorder[0:root_idx]
                left_pre = preorder[1:1+root_idx]
            root.left = self.rebuildBinaryTree(left_pre,left_in)
        if root_idx != len(inorder)-1: # right exist
            right_in = [inorder[-1]]
            right_pre = [preorder[-1]]
            if root_idx < len(inorder)-2:
                right_in = inorder[root_idx+1:]
                right_pre = preorder[root_idx+1:]
            root.right = self.rebuildBinaryTree(right_pre,right_in)
        return root

slt = Solution()
preorder = [1,2,4,5,7,8,3,6,9,10,11]
inorder = [4,2,5,8,7,1,6,10,9,11,3]
root = slt.rebuildBinaryTree(preorder,inorder)
print(preorder)
print(slt.traversingInPreorder(root))
print(inorder)
print(slt.traversionInInOrder(root))





