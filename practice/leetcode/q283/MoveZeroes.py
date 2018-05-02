"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        i = 0
        begin =0
        move = 0
        while True:
            if begin + zeros == len(nums):
                break
            while nums[i] == 0:
                zeros = zeros+1
                i = i+1


if __name__ == '__main__':
    array = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(array)
    print(array)