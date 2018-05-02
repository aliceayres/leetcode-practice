"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def log(self):
        print('------')
        p = self
        while True:
            print(p.val)
            p = p.next
            if p == None:
                break
        print('------')

# Solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        store = 0
        p = l1
        q = l2
        original = ListNode(-1)
        node = original
        while True:
            if p != None:   # attention p or q is None
                v1 = p.val
            else:
                v1 = 0
            if q != None:
                v2 = q.val
            else:
                v2 = 0
            sum = v1 + v2 + store
            if sum > 9:
                store = sum//10  # floor
            else:
                store = 0
            node.next = ListNode(sum % 10)
            if p != None:
                p = p.next
            if q != None:
                q = q.next
            node = node.next
            if p == None and q == None: # break condition
                if store != 0:
                    node.next = ListNode(store)
                break
        return original.next

    def transform(self, array):
        original = ListNode(array[0])
        node = original
        for i in range(1,len(array)):
            node.next = ListNode(array[i])
            node = node.next
        return original

if __name__ == '__main__':
    a = [8,9,9]
    b = [2]
    s = Solution()
    node1 = s.transform(a)
    node2 = s.transform(b)
    sum = s.addTwoNumbers(node1,node2)
    node1.log()
    node2.log()
    sum.log()
