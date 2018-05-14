"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:
Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    def singleNumberUsingExtra(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for x in nums:
            cache[x] = cache.get(x, 0) + 1
        for item in cache.items():
            if item[1] == 1:
                return item[0]

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
            result ^= x
        return result

if __name__ == '__main__':
    slt = Solution()
    nums = [1,2,1,2,3,3,4,19,4]
    print(slt.singleNumber(nums))