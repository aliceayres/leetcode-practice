"""
387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        for x in s:
            cache[x] = cache.get(x,0)+1
        for i in range(len(s)):
            if cache[s[i]] == 1:
                return i
        return -1