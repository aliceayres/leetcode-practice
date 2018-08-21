"""
796. Rotate String
We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
Return True if and only if A can become B after some number of shifts on A.
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true
Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:
A and B will have length at most 100.
"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        for i in range(len(A)):
            if B[0] == A[i]:
                if i == 0:
                    if A == B:
                        return True
                else:
                    if A[i:] + A[0:i] == B: # 0~i-1 → [0:i]
                        return True
        return False

if  __name__ == '__main__':
    slt = Solution()
    a = 'abced'
    b = 'cedab'
    print(slt.rotateString(a,b))






