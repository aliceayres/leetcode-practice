"""
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum
area is 0.)
Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected
4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        cache = {}
        m = len(grid[0])
        n = len(grid)
        max = 0

        for i in range(n):
            for j in range(m):
                stack = []
                area = 0
                if cache.get((i,j)) == None and grid[i][j] != 0: # the element did't check
                    # begin find
                    cache.setdefault((i,j),1)
                    current = None
                    stack.append((i,j))
                    while len(stack) > 0:
                        current = stack.pop(-1)
                        print(current)
                        area = area + 1
                        row = current[0]
                        col = current[1]
                        if row != 0:
                            if grid[row-1][col] ==1 and cache.get((row-1,col)) == None:
                                stack.append((row-1,col))
                                cache.setdefault((row-1,col),1)
                        if col != m-1 and cache.get((row,col+1)) == None:
                            if grid[row][col+1] ==1:
                                stack.append((row,col+1))
                                cache.setdefault((row, col+1), 1)
                        if row != n-1 and cache.get((row+1,col)) == None:
                            if grid[row+1][col] ==1:
                                stack.append((row+1, col))
                                cache.setdefault((row+1, col), 1)
                        if col != 0 and cache.get((row,col-1)) == None:
                            if grid[row][col-1] ==1:
                                stack.append((row,col-1))
                                cache.setdefault((row, col-1), 1)
                if area > max:
                    max = area

        return max


if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    s = Solution()
    maxIsland = s.maxAreaOfIsland(grid)
    print(maxIsland)