"""
448. Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [i for i in range(1,len(nums)+1)]
        for x in nums:
            result[x-1] = 0
        i = 0
        while i< len(result):
            if result[i] == 0:
                result.pop(i)
            else:
                i += 1
        return result

if __name__ == '__main__':
    slt = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(slt.findDisappearedNumbers(nums))