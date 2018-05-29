"""
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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

    def concat(self,node,tail):
        nd = node
        while nd.next != None:
            nd = nd.next
        nd.next = tail
        return node

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        """
        if the two linked lists have intersection,
        and if you go through A + B vs B + A,
        you should see the intersection node at some point
        e.g. A: a1, a2, c1, c2, c3, B: b1, b2, b3, c1, c2, c3
        A -> B (link B to the end of A): a1, a2, c1, c2, c3, b1, b2, b3, c1, c2, c3
        B -> A (link A to the end of B): b1, b2, b3, c1, c2, c3, a1, a2, c1, c2, c3
        As you can see, the intersection is at c1 (the third element from the tail)
        If there's no intersection, the loop will exit because both pointer is None
        """
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa if pa is not None else None

if __name__ == '__main__':
    slt = Solution()
    a = slt.transform([1,2])
    b = slt.transform([12,17,19])
    c = slt.transform([4,7,9])
    d = slt.getIntersectionNode(slt.concat(a,c),slt.concat(b,c))
    print(slt.detransform(d))