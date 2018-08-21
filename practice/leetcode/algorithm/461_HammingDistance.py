"""
461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Seen this ques
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binX = bin(x)[2:].rjust(32,'0')
        binY = bin(y)[2:].rjust(32,'0')
        distance = 0
        for i in range(len(binX)):
            if binX[i] != binY[i]:
                distance += 1
        return distance

    def hammingDistanceBest(self,x,y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        y = 0
        while (x): # x & x-1 operation
            y += 1
            x &= x - 1
        return y

if __name__ == '__main__':
    x = 1
    y = 3
    s = Solution()
    distance = s.hammingDistanceXOR(x,y)
    print(distance)