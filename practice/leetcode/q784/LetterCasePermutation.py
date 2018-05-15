"""
784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase
or uppercase to create another string.  Return a list of all possible strings
we could create.
Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
Input: S = "3z4"
Output: ["3z4", "3Z4"]
Input: S = "12345"
Output: ["12345"]
Note:
S will be a string with length at most 12.
S will consist only of letters or digits.
"""


class Solution:
    def letterCasePermutation(self, S):
        if len(S) == 0:
            return [""]
        others = self.letterCasePermutation(S[1:])
        return [S[0].lower() + t for t in others]+[S[0].upper() + t for t in others] if S[0].isalpha() else [S[0]+ t for t in others]

    def letterCasePermutationByStandard(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        letters = 0
        for x in S:
            if not x.isdigit():
                letters += 1
        if letters == 0:
            return [S]
        right = int(''.join(['1' for i in range(letters)]), 2)
        result = []
        for i in range(right + 1):
            standard = bin(i)[2:]
            prefix = ['0' for i in range(letters - len(standard))]
            standard = ''.join(prefix) + standard
            j = 0
            str = []
            for ch in S:
                r = ch
                if not ch.isdigit():
                    if ch.isupper() and standard[j] == '0':
                        r = ch.lower()
                    elif ch.islower() and standard[j] == '1':
                        r = ch.upper()
                    j += 1
                str.append(r)
            result.append(''.join(str))
        return result

if __name__ == '__main__':
    slt = Solution()
    print(slt.letterCasePermutation('a1b2c3'))

