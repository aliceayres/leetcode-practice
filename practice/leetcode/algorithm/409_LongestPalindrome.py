"""
409. Longest Palindrome
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        for x in s:
            cache[x] = cache.get(x, 0) + 1
        length = 0
        single = 0
        for item in cache.items():
            if item[1] % 2 == 0:
                length += item[1]
            else:
                if single == 0:
                    single = 1
                if item[1] > 2:
                    length += item[1] - 1
        return length + single