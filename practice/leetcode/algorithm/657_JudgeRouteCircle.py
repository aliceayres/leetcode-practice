"""
657. Judge Route Circle
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge
if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should
 be true or false representing whether the robot makes a circle.
Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr = 0
        ud = 0
        for ch in moves:
            if ch == "L":
                lr += 1
            elif ch == "R":
                lr -= 1
            elif ch == "U":
                ud += 1
            elif ch == "D":
                ud -= 1
        return lr == 0 and ud == 0 # moves.count('U')

if __name__ == '__main__':
    moves = "URLDLR"
    s = Solution()
    isCircle = s.judgeCircle(moves)
    print(isCircle)