"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def transform(self,array):
        head = ListNode(0)
        pre = head
        for x in array:
            current = ListNode(x)
            pre.next = current
            pre = current
        return head.next

    def detransform(self,node):
        array = []
        nd = node
        while nd != None:
            array.append(nd.val)
            nd = nd.next
        return array

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        p = l1
        q = l2
        while p != None or q != None:
            if p == None:
                current.next = q
                break
            if q == None:
                current.next = p
                break
            if p.val < q.val:
                current.next = p
                p = p.next
            else:
                current.next = q
                q = q.next
            current = current.next
        return head.next

if __name__ == '__main__':
    slt = Solution()
    l1 = slt.transform([1,2,3])
    l2 = slt.transform([2,4,7,8])
    head = slt.mergeTwoLists(l1,l2)
    print(slt.detransform(head))