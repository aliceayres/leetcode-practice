class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums == []:  # empty
            return nums
        m = len(nums[0])
        n = len(nums)
        if m*n > r*c:  # impossible fill orginal
            return nums
        if m<=c and n<=r: # the same
            return nums
        # normal situation
        begin = 0
        line = 0
        reshape = [[] for i in range(r)]
        for k in range(0,r):
            count = c # to get count, every row begin count=c
            while count > 0:
                if begin > m-1:
                    begin = 0
                    line = line +1
                last = min(begin+count-1,m-1)
                if begin != last+1:
                    reshape[k].extend(nums[line][begin:last+1])
                else:
                    reshape[k].append(nums[line][begin])
                count = count - last+begin-1
                begin = last + 1
        return reshape

if __name__ == '__main__':
    matrix = [[1,2],[3,4]]
    s = Solution()
    reshape = s.matrixReshape(matrix,4,1)
    print(reshape)