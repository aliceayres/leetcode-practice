"""
557. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.
Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not
be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = s.split(' ')
        return ' '.join([self.reverse(x) for x in array])

    def reverse(self, s):
        return ''.join([s[-i] for i in range(1, len(s) + 1)])

if __name__ == '__main__':
    a = "let's leetcode everyday now"
    s = Solution()
    c = s.reverseWords(a)
    print(c)
