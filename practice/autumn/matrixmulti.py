'''
matrix multiplication 矩阵乘法
'''


class Solution:
    def solute(self,left,right):
        m = len(left) # row of left : matrix row
        n = len(right[0]) # col of right : matrix col
        p = len(left[0]) # col of left
        matrix = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                sum = 0
                for k in range(p):
                    sum += left[i][k]*right[k][j]
                matrix[i].append(sum)
        print(matrix)
        for i in range(m):
            for j in range(n):
                print(matrix[i][j])

if __name__ == '__main__':
    slt = Solution()
    a = [[1,1],[1,0]]
    b = [[1,1],[1,0]]
    print(slt.solute(a,b))