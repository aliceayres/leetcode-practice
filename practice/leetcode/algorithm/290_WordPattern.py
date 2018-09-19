'''
290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        array = str.split(' ')
        cache = {}
        pattern_map = {}
        if len(array) != len(pattern):
            return False
        for i in range(len(array)):
            word = array[i]
            pt = pattern[i]
            if pattern_map.get(pt) is None:
                if cache.get(word) is None:
                    pattern_map[pt] = word
                    cache[word] = pt
                else:
                    return False
            else:
                if pattern_map[pt] != word:
                    return False
        return True

if __name__ == '__main__':
    s = 'dog cat cat dog'
    s1 = 'dog dog dog dog'
    s2 = 'dog cat cat fish'
    pattern = 'abba'
    slt = Solution()
    print(slt.wordPattern(pattern,s))
    print(slt.wordPattern(pattern, s1))
    print(slt.wordPattern(pattern, s2))