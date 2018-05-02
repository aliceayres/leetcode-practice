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