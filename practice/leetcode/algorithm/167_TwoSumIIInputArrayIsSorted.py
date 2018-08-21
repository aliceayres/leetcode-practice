"""
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        current = -1
        for i in range(len(numbers)):
            if current == -1:
                current = numbers[i]
            else:
                if numbers[i] == current:
                    continue
                else:
                    current = numbers[i]
            if numbers[i] > target:
                return []
            else:
                find = target - numbers[i]
                if i == len(numbers) - 1:
                    return []
                j = i + 1
                while j < len(numbers):
                    if numbers[j] == find:
                        return [i + 1, j + 1]
                    if numbers[j] > find:
                        break
                    j += 1

if __name__ == '__main__':
    slt = Solution()
    numbers = [2,7,8,12,15,78]
    target = 9
    print(slt.twoSum(numbers,target))


