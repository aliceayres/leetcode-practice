"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}  # map the nums : value -> i
        cache_repeated = {} # map repeated value (two sum)
        for i in range(0,len(nums)):
            key = nums[i]
            if cache.get(key) != None: # dict get key function
                cache_repeated[key] = i
            else:
                cache[key] = i
        for i in range(0,len(nums)):
            key = target - nums[i]
            if key != nums[i]:
                if cache.get(key) != None:
                    return [i,cache[key]]
            else:
                if cache_repeated.get(key) != None:
                    return[i,cache_repeated[key]]
        return []

if __name__ == '__main__':
    nums = [3,2,4]
    s = Solution()
    indexes = s.twoSum(nums,6)
    print(indexes)