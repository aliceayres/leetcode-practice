"""
561. Array Partition I
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as
large as possible.
Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = nums[:] # copy original array
        Solution.partition(self, numbers, 0, len(nums) - 1) # quick sort
        sum = 0
        for i in range(0, len(numbers), 2): # range(start,len,step)
            sum = sum + numbers[i]
        return sum

    def partition(self, nums, left, right):
        if left > right:
            return
        i = left
        j = right
        base = nums[left]
        while i < j:
            while (i != j and base <= nums[j]):
                j = j - 1
            nums[i] = nums[j]
            while (i != j and base >= nums[i]):
                i = i + 1
            nums[j] = nums[i]
        nums[i] = base
        Solution.partition(self, nums, left, i - 1)
        Solution.partition(self, nums, i + 1, right)
        return nums

if __name__ == '__main__':
    nums = [1,2,3,2]
    s = Solution()
    sum = s.arrayPairSum(nums)
    print(sum)