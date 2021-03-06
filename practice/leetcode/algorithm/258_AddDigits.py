"""
258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        st = str(num)
        while len(st) > 1:
            sum = 0
            for x in st:
                sum += int(x)
            st = str(sum)
        return int(st)

    def addDigitsNoLoop(self, num): # num%9
        if num % 9 == 0:
            return 0 if num == 0 else 9
        else:
            return num % 9

if __name__ == '__main__':
    slt = Solution()
    print(slt.addDigitsNoLoop(38))