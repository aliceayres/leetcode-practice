"""

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