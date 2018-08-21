"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:  # None
            return True
        single = head
        double = head
        flag = False
        middle = head
        while double != None:  # find middle
            if flag and single == double:
                break
            else:
                middle = single
                single = single.next
                double = double.next
                if double != None:
                    double = double.next

        if middle.next == None:  # only 2 node
            return head.val == middle.val
        pre = middle.next
        node = pre.next
        while node != None:  # reverse
            pre.next = node.next
            node.next = middle.next
            middle.next = node
            node = pre.next
        before = head
        after = middle.next
        while after != None:  # compare
            print(before.val, after.val)
            if before.val != after.val:
                return False
            before = before.next
            after = after.next
        return True