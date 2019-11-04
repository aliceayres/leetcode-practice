'''
Cut Rod 钢条切割
'''


class Solution:
    def __init__(self):
        self.cache = []
        self.prices = []

    def cut_rod_memo(self,n):
        if self.cache[n] >= 0:
            return self.cache[n]
        if n == 0:
            self.cache[n] = 0
            return 0
        r = -1
        for i in range(1, n + 1):  # range [1,n]
            r = max(r, self.prices[i - 1] + self.cut_rod_memo(n - i))
        self.cache[n] = r
        return r

    def cut_rod_memo_func(self,n):
        if len(self.cache) == 0:
            self.cache += [-1 for i in range(n+1)]
        return self.cut_rod_memo(n)


    def cut_rod_naive(self,n):
        if n == 0:
            return 0
        r = -1
        for i in range(1,n+1): # range [1,n]
            r = max(r,self.prices[i-1]+self.cut_rod_naive(n-i))
        return r

    def solute(self):
        self.prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10
        print(self.cut_rod_naive(n))
        print(self.cut_rod_memo_func(n))
        print(self.cache)
        return


if __name__ == '__main__':
    slt = Solution()
    slt.solute()