'''
884. Uncommon Words from Two Sentences
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words.
You may return the list in any order.
Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
Note:
0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
'''

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        aa = A.split(' ')
        bb = B.split(' ')
        ca = {}
        cb = {}
        result = []
        for a in aa:
            if ca.get(a,0) != 0:
                ca[a] += 1
            else:
                ca.setdefault(a,1)
        for b in bb:
            if cb.get(b,0) != 0:
                cb[b] += 1
            else:
                cb.setdefault(b,1)
        for a in aa:
            if cb.get(a,0) == 0 and ca[a] == 1:
                result.append(a)
        for b in bb:
            if ca.get(b,0) == 0 and cb[b] == 1:
                result.append(b)
        return result

if __name__ == '__main__':
    s1 = 'this is sweet'
    s2 = 'this is sour'
    slt = Solution()
    print(slt.uncommonFromSentences(s1, s2))