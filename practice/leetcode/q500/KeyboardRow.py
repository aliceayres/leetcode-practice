"""
500. Keyboard Row
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.
American keyboard
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        key = [('qwertyuiop',1),('asdfghjkl',2),('zxcvbnm',3)]
        mapping = [0 for i in range(26)]
        for e in key:
            for ch in e[0]:
                mapping[ord(ch)-ord('a')] = e[1]
        result = []
        for word in words:
            first = word[0].lower()
            line = mapping[ord(first)-ord('a')]
            same_row = True
            for ch in word.lower()[1:]:
                if line != mapping[ord(ch)-ord('a')]:
                    same_row = False
                    break
            if same_row:
                result.append(word)
        return result

if __name__ == '__main__':
    a = ["Hello", "Alaska", "Dad", "Peace"]
    s = Solution()
    c = s.findWords(a)
    print(c)
