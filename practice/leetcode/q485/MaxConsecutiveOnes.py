"""
485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = 0
        consecutive = 0
        store = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                begin = i
                store = 0
            if nums[i] == 1:
                end = i
                store = store + 1
                consecutive = max(store, consecutive)
        return consecutive

if __name__ == '__main__':
    a = [1,1,0,1,1,1,1,0,1,0,1,0,0]
    s = Solution()
    consecutive = s.findMaxConsecutiveOnes(a)
    print(consecutive)