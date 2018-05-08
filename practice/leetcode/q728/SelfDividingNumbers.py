"""
728. Self Dividing Numbers
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.
Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for x in range(left,right+1):
            if self.isSelfDividing(x):
                result.append(x)
        return result

    def isSelfDividing(self,x):
        y = x
        while y != 0:
            m = y % 10
            if m == 0:
                return False
            if x % m != 0:
                return False
            y = y//10
        return True

if __name__ == '__main__':
    s = Solution()
    result = s.selfDividingNumbers(1,22)
    print(result)