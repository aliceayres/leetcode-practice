"""
141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        double = head
        flag = False
        while double != None:
            if flag and node == double:
                return True
            if flag == False:
                flag = True
            node = node.next
            double = double.next
            if double != None:
                double = double.next
        return False
