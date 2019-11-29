'''
15.4 LCS longest common subsequence 最长公共子序列
暴力求解 m*2^n
递归求解 2^(m+n)
动态规划 time → mn + (m+n)，space → mn
动态规划优化 space → min(m,n)+o(1) 15.4-4
'''

class Solution:
    def dpopt(self,x,y): # 优化空间的动态规划 15.4-4
        fix = x
        scan = y
        if len(y) < len(x):
            fix = y
            scan = x
        c = [0 for i in range(len(fix))] # min(m,n) → c & o(1) → diagonal
        for i in range(len(scan)):
            diagonal = 0
            for j in range(len(fix)):
                if scan[i] == fix[j]:
                    tmp = c[j]
                    c[j] = diagonal + 1
                    diagonal = tmp
                else:
                    before = 0
                    old = c[j]
                    if j != 0:
                        before = c[j-1]
                    c[j] = old
                    if before > old:
                        c[j] = before
                    diagonal = old
        print(c)
        k = len(c) - 1
        p = len(scan) - 1
        lcs = ''
        while k >= 0 and p >= 0 and c[k] > 0:
            current_length = c[k]
            if fix[k] == scan[p]:
                lcs = fix[k] + lcs
                i = k - 1
                while c[i] == current_length > 1:
                    c[i] = c[i] - 1
                    i -= 1
                p = p - 1
                k = k - 1
            else:
                j = k - 1
                while c[j] == current_length:
                    if fix[j] == scan[p]:
                        k = j
                        break
                    else:
                        j = j - 1
                if fix[k] != scan[p]:
                    p = p - 1
        return lcs

    def dp(self,x,y):  # 自底向上的动态规划
        c = [[None for j in range(len(y))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    c[i][j] = 1
                    if i != 0 and j != 0:
                        c[i][j] = c[i-1][j-1] + 1
                else:
                    t = 0
                    q = 0
                    if i != 0:
                        t = c[i-1][j]
                    if j != 0:
                        q = c[i][j-1]
                    c[i][j] = t
                    if q > t:
                        c[i][j] = q
        i = len(x) - 1
        j = len(y) - 1
        lcs = ''
        while i >= 0 and j >= 0:
            if x[i] == y[j]:
                lcs = x[i] + lcs
                i = i - 1
                j = j - 1
            else:
                if i == 0 or j == 0:
                    break
                if c[i-1][j] >= c[i][j-1]:
                    i = i - 1
                else:
                    j = j - 1
        return lcs

    def memoization(self,x,y,i,j,cache): # 备忘法
        if i == 0 or j == 0:
            if i == 0 and y[:j+1].find(x[0]) != -1:
                cache[i][j] = x[0]
            elif j == 0 and x[:i+1].find(y[0]) != -1:
                cache[i][j] = y[0]
            else:
                cache[i][j] = ''
        elif x[i] == y[j]:
            if cache[i-1][j-1] is None:
                cache[i-1][j-1] = self.memoization(x,y,i-1,j-1,cache)
            cache[i][j] = cache[i-1][j-1]+x[i]
        else:
            if cache[i-1][j] is None:
                cache[i-1][j] = self.memoization(x,y,i-1,j,cache)
            if cache[i][j-1] is None:
                cache[i][j-1] = self.memoization(x, y,i,j-1,cache)
            cache[i][j] = cache[i-1][j]
            if len(cache[i][j-1]) > len(cache[i-1][j]): # or >=
                cache[i][j] = cache[i][j-1]
        return cache[i][j]

    def solute(self,x,y): # 递归 2^(m+n)
        if len(x) == 1 and y.find(x) != -1:
            return [x]
        if len(y) == 1 and x.find(y) != -1:
            return [y]
        if len(x) == 1 or len(y) == 1:
            return []
        if x[-1] == y[-1]:
            lcs_array = self.solute(x[:-1],y[:-1])
            return [e+x[-1] for e in lcs_array]
        else:
            left = self.solute(x[:-1],y)
            right = self.solute(x,y[:-1])
            # return left + right
            if len(left) !=0 and len(right) != 0:
                if len(left[0]) == len(right[0]):
                    return left + right
                elif len(left[0]) > len(right[0]):
                    return left
                else:
                    return right
            else:
                return left + right

if __name__ == '__main__':
    slt = Solution()
    x = 'ABCBDAB'
    y = 'BDCABA'
    cache = [[None for j in range(len(y))] for i in range(len(x))]
    rs = slt.memoization(x,y,len(x)-1,len(y)-1,cache)
    print(rs)
    # for e in cache:
    #     print(e)
    print(slt.dp(x,y))
    print(slt.dpopt(x,y))
    # r = slt.solute(x,y)
    # print(set(r))
    # 15.4-1
    t = '10010101'
    s = '010110110'
    print(slt.dpopt(t,s))
