"""
389. Find the Difference
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.
Example:
Input:
s = "abcd"
t = "abcde"
Output:
e
Explanation:
'e' is the letter that was added.
"""

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for x in set(t): # set()
            if x not in set(s) or s.count(x) < t.count(x): # str.count()
                return x

if __name__ == '__main__':
    s = 'a'
    t = 'aa'
    solution = Solution()
    print(solution.findTheDifference(s,t))