"""
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        cache = {}
        for i in range(len(s)):
            cache[s[i]] = cache.get(s[i], 0) + 1
            cache[t[i]] = cache.get(t[i], 0) - 1
        for item in cache.items():
            if item[1] != 0:
                return False
        return True
