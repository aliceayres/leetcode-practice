"""
594. Longest Harmonious Subsequence
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for x in nums:
            cache[x] = cache.get(x, 0) + 1
        longest = 0
        for item in cache.items():
            if item[0] - 1 in cache:
                ll = cache[item[0] - 1] + item[1]
                if ll > longest:
                    longest = ll
            if item[0] + 1 in cache:
                lr = cache[item[0] + 1] + item[1]
                if lr > longest:
                    longest = lr
        return longest