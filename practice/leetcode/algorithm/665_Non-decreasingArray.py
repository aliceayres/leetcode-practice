"""
665. Non-decreasing Array
Given an array with n integers,
your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if i - 1 >= 0 and i + 2 <= len(nums)-1:
                   if nums[i-1] > nums[i+1] and nums[i] > nums[i+2]:
                       return False
                count += 1
            if count > 1:
                return False
        return True

if __name__ == '__main__':
    slt = Solution()
    print(True == slt.checkPossibility([2, 3, 3, 2, 4]))
    print(True == slt.checkPossibility([2, 1, 1, 1, 1]))
    print(True == slt.checkPossibility([1, 6, 5, 14, 17]))
    print(False == slt.checkPossibility([3, 4, 2, 3, 5]))