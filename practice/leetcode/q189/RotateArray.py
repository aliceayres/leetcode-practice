"""
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    def rotates(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k %= len(nums)
        if k == 0:
            return
        loop = -1
        i = 0
        before = nums[0]
        count = 1
        bound = len(nums)-k
        while count <= len(nums):
            if loop == -1:
                loop = i
            else:
                if i == loop:
                    i += 1
                    before = nums[i]
                    loop = -1
                    continue
            to = i - bound
            if i < bound:
                to = i+k
            tmp = nums[to]
            nums[to] = before
            before = tmp
            print(nums, i, before,count)
            i = to
            count += 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k %= len(nums)
        if k == 0:
            return
        bound = len(nums) - k
        cache = nums[bound:]
        for i in range(bound):
            idx = bound - 1 - i
            nums[idx+k] = nums[idx]
        for i in range(len(cache)):
            nums[i] = cache[i]

if __name__ == '__main__':
    slt = Solution()
    nums = [1,2,3,4,5,6]
    k = 2
    slt.rotates(nums,k)
    print(nums)