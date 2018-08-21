"""
821. Shortest Distance to a Character
Given a string S and a character C, return an array of integers representing
the shortest distance from the character C in the string.
Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        cache = []
        result = []
        for i in range(len(S)):
            if S[i] == C:
                cache.append(i)
        for j in range(len(S)):
            if S[j] == C:
                result.append(0)
            else:
                candidate = self.candidate(j,cache)
                result.append(candidate)
        return result

    def candidate(self,x,cache):
        binary = self.binary(x, cache)
        pos = binary[1]
        if binary[0]:
            if pos - 1 < 0:
                return (cache[pos] - x)
            else:
                return min((cache[pos] - x), (x - cache[pos - 1]))
        else:
            if pos + 1 > len(cache)-1:
                return (x - cache[pos])
            else:
                return min((cache[pos+1]-x),(x-cache[pos]))

    def binary(self,x,sorted):
        left = 0
        right = len(sorted)-1
        last = 0
        while True:
            median = (left+right)//2
            if sorted[median] > x:
                left = left
                right = median - 1
                if right < 0:
                    last = 0
                else:
                    last = right # attention when last
            else:
                left = median + 1
                right = right
                if left > len(sorted)-1:
                    last = len(sorted)-1 # attention boundary
                else:
                    last = left
            if right <= left: # attention break condition
                break
        return (sorted[last] > x,last)

if __name__ == '__main__':
    S = "rfnlmxhnpifuaxinxpxlcttjnlggmkjioewbecnofqpvcikiazmnghehfmcpwsmjtmgvsxtogcguykfmncglcbrafjljvpivdolj"
    C = "c"
    s = Solution()
    result = s.shortestToChar(S,C)
    print(result)