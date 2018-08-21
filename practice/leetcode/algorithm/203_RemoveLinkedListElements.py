"""
203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = head
        node = head
        while node != None:
            if node.val == val:
                if node == head:
                    head = node.next
                else:
                    pre.next = node.next
                    node = node.next
            else:
                pre = node
                node = node.next
        return head
