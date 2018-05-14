"""
463. Island Perimeter
You are given a map in form of a two-dimensional integer grid where 1 represents land and
0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
he grid is completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells). The island doesn't have "lakes" (water inside that isn't
connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of
the island.
Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""


class Solution:
    def islandPerimeter(self, grid):  # not required to draw the island so don't need backtracking
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        i = 0
        j = 0
        stack = []
        island = {}
        total = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if island.get((i, j), -1) != -1:
                    continue
                stack.append((i, j))
                while len(stack) != 0:
                    count = 0
                    current = stack.pop(-1)
                    ii = current[0]
                    jj = current[1]
                    if island.get((ii, jj), -1) != -1:
                        continue
                    if ii - 1 >= 0:
                        if grid[ii - 1][jj] == 1:
                            stack.append((ii - 1, jj))
                            count += 1
                    if ii + 1 <= n - 1:
                        if grid[ii + 1][jj] == 1:
                            stack.append((ii + 1, jj))
                            count += 1
                    if jj - 1 >= 0:
                        if grid[ii][jj - 1] == 1:
                            stack.append((ii, jj - 1))
                            count += 1
                    if jj + 1 <= m - 1:
                        if grid[ii][jj + 1] == 1:
                            stack.append((ii, jj + 1))
                            count += 1
                    island.setdefault(current, 4 - count)
                    total += 4 - count
        return total

if __name__ == '__main__':
    a = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    s = Solution()
    c = s.islandPerimeter(a)
    print(c)