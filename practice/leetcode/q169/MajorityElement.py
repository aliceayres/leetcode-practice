"""
169. Majority Element
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for x in nums:
            cache[x] = cache.get(x, 0) + 1
            if cache[x] > len(nums) // 2:
                return x

if __name__ == '__main__':
    slt = Solution()
    print(slt.majorityElement([2,1,3,2,2,2]))