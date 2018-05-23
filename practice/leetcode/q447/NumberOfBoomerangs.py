"""
447. Number of Boomerangs
Given n points in the plane that are all pairwise distinct,
a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j
equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs.
You may assume that n will be at most 500 and coordinates of points are all in the
range [-10000, 10000] (inclusive).
Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2
Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cache = {} # index,distance : count
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    distance = (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                    key = (i,distance)
                    cache[key] = cache.get(key,0) + 1
        sum = 0
        for item in cache.items():
            if item[1] > 1:
                sum += item[1]*(item[1]-1) # not factorial! just 2
        return sum