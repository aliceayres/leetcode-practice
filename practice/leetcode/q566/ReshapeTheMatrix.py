"""
566. Reshape the Matrix
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into
 a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and
 c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same
 row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped
 matrix; Otherwise, output the original matrix.
Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row
by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""

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