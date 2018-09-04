'''
4. 从尾到头打印链表
题目描述：
输入链表的第一个节点，从尾到头反过来打印出每个结点的值。
'''

class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def transformListToLink(self, array):
        last = None
        i = len(array)-1
        while i >= 0:
            node = LinkNode(array[i])
            node.next = last
            i -= 1
            last = node
        return last

    def invertedLinkList(self, node):
        cur = node
        stack = []
        inverted = []
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        while len(stack) > 0:
            inverted.append(stack.pop(-1).value)
        return inverted

slt = Solution()
numbers = [1,2,3,4,5,6]
print(slt.invertedLinkList(slt.transformListToLink(numbers)))




