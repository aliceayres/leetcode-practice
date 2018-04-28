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