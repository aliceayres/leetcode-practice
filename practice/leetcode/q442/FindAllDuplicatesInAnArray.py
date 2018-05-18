"""
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [] # original array as map
        for x in nums:
            if nums[abs(x)-1] < 0:
                result.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return result

if __name__ == '__main__':
    slt = Solution()
    nums  = [2,3,6,5,1,9,3,2,6]
    print(slt.findDuplicates(nums))