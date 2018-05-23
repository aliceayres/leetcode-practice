"""
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cache = {i: 0 for i in nums1}
        result = {}
        for x in nums2:
            if x in cache:
                result.setdefault(x, 0)
        return [item[0] for item in result.items()]
