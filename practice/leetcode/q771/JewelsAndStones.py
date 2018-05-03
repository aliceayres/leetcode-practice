"""
771. Jewels and Stones
You're given strings J representing the types of stones that are jewels, and S
representing the stones you have.  Each character in S is a type of stone you
have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".
Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:
Input: J = "z", S = "ZZ"
Output: 0
Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        map = {}
        for i in range(len(S)):
            value = map.get(S[i],0)
            map[S[i]] = value + 1
        count = 0
        for j in range(len(J)):
            value = map.get(J[j])
            if value != None:
                count += value
        return count

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    s = Solution()
    count = s.numJewelsInStones(jewels,stones)
    print(count)