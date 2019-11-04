'''
Cut Rod 钢条切割
15.1-3 固定成本c
'''


class Solution:
    def __init__(self):
        self.cache = []
        self.cache_cut = []
        self.prices = []
        self.cost = 1

    def cut_rod(self,n):
        memo = [0]+ [-1 for i in range(n)]
        cuts = [0]+ [-1 for i in range(n)]
        counts = [0]+ [0 for i in range(n)]
        for i in range(1,n+1):
            for j in range(1, i+1):
                count = counts[i - j]
                if j != i:
                    count += 1
                r = self.prices[j - 1] + memo[i - j] - self.cost * count
                if memo[i] < r:
                    memo[i] = r
                    cuts[i] = j
                    counts[i] = count

        print(memo)
        print(cuts)
        print(counts)
        return memo[n]

    def cut_rod_memo(self,n):
        if self.cache[n] >= 0:
            return self.cache[n]
        if n == 0:
            self.cache[n] = 0
            self.cache_cut[n] = 0
            return 0
        r = -1
        for i in range(1, n + 1):  # range [1,n]
            sub = self.prices[i - 1]+self.cut_rod_memo(n - i)
            if r < sub:
                r = sub
                self.cache_cut[n] = i
        self.cache[n] = r
        return r

    def cut_rod_memo_func(self,n):
        if len(self.cache) == 0:
            self.cache += [-1 for i in range(n+1)]
            self.cache_cut += [-1 for i in range(n + 1)]
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
        print(self.cache_cut)
        print(self.cut_rod(n))
        return


if __name__ == '__main__':
    slt = Solution()
    slt.solute()