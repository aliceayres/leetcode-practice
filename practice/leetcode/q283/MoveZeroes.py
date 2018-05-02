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
        total = 0
        begin = 0
        pos = 0
        c = 0
        while True:
            if pos + total == len(nums):
                break
            zeros = 0
            i = begin
            while i < len(nums) and nums[i] == 0 :
                zeros = zeros+1
                i = i+1
                c = c + 1
                print(c)
            move = i
            j = pos
            while move < len(nums) and nums[move] != 0:
                nums[j] = nums[move]
                j = j + 1
                move = move +1
                c = c + 1
                print(c)
            begin = move
            pos = j
            total = total + zeros
        for k in range(pos,len(nums)):
            nums[k] = 0

    def moveZerosBySwap(self, nums):
        for i in range(len(nums)):
            if nums[i] ==0:
                for j in range(i,len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[i]+nums[j]
                        nums[j] = nums[i]-nums[j]
                        nums[i] = nums[i]-nums[j]
                        break

if __name__ == '__main__':
    array = [0,0,4,0,5,0,0,1,3,7,8,0,12]
    s = Solution()
    s.moveZeroes(array)
    print(array)