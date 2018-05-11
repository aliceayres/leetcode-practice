"""
344. Reverse String
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([s[-i] for i in range(1,len(s)+1)])

if __name__ == '__main__':
    str = "iloveleetcode"
    s = Solution()
    reverse = s.reverseString(str)
    print(reverse)