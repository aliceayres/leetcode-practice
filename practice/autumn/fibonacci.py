'''
Fibonacci
'''


class Solution:
    def solute(self,n):
        return self.matrix(n)

    def naive(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return self.naive(n-1)+self.naive(n-2)

    def bottom(self,n):
        cache = []
        for i in range(n+1):
            if i == 0:
                cache += [0]
            elif i == 1:
                cache += [1]
            else:
                cache += [cache[i-1] + cache[i-2]]
        return cache[n]

    def matrixmulti(self,a,b):
        m = len(a)
        n = len(b[0])
        p = len(a[0])
        matrix = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                sum = 0
                for k in range(p):
                    sum += a[i][k]*b[k][j]
                matrix[i].append(sum)
        return matrix

    def matrixpower(self,matrix,n):
        power = matrix
        for i in range(n-1):
            power = self.matrixmulti(power,matrix)
        return power

    def matrix(self,n):
        mt = [[1,1],[1,0]]
        fb = self.matrixpower(mt,n-1)
        return fb[0][0]

if __name__ == '__main__':
    slt = Solution()
    n = 10
    fb = slt.solute(n)
    print(fb)