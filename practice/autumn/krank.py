'''
选择问题
Kth smallest rank 第k小的值
堆排序 归并排序 nlgn
rand-select 期望线性时间 所有元素互异 n 最坏 n^2 按余下元素中最大的划分
rand-select-loop 基于循环 9.2-3
select 最坏线性时间 n
'''

import random

class Solution:
    def solute(self,num,k):
        return self.select(num,0,len(num)-1,k)

    def insertion_mid(self,num,begin,end):
        mid = (begin+end)//2
        for i in range(begin+1,end+1):
            n = num[i]
            j = i - 1
            while(j >= begin and num[j] > n):
                num[j+1] = num[j]
                j -= 1
            num[j+1] = n
        return mid

    def select(self,num,begin,end,k):
        if begin == end:
            return num[begin]
        i = begin
        cache = {} # cache mid:index
        while i <= end:
            ii = i+4
            if i+4 > end:
                ii = end
            mid_idx = self.insertion_mid(num,i,ii)
            i += 5
            cache[num[mid_idx]] = mid_idx
        mids = list(cache.keys())
        k_mid = (len(mids)-1)//2+1
        x = self.select(mids,0,len(mids)-1,k_mid)
        index = cache[x]
        pivot = self.partition(num,begin,end,index=index)
        if k == pivot+1-begin:    # don't forget begin
            return num[pivot]
        elif k < pivot+1-begin:
            return self.select(num,begin,pivot-1,k)
        else:
            return self.select(num,pivot+1,end,k-pivot-1+begin)

    def rand_select(self,num,begin,end,k):
        if begin == end:
            return num[begin]
        pivot = self.partition(num,begin,end)
        if k == pivot+1-begin:    # don't forget begin
            return num[pivot]
        elif k < pivot+1-begin:
            return self.rand_select(num,begin,pivot-1,k)
        else:
            return self.rand_select(num,pivot+1,end,k-pivot-1+begin)


    def rand_select_loop(self,num,p,q,r):
        begin = p
        end = q
        kk = r
        while True:
            if begin == end:
                return num[begin]
            pivot = self.partition(num, begin, end)
            if kk == pivot + 1 - begin:  # don't forget begin
                return num[pivot]
            elif kk < pivot + 1 - begin:
                end = pivot - 1
            else:
                kk = kk - pivot - 1 + begin  # here begin will change , calculate new kk first!
                begin = pivot + 1


    def partition(self,num,begin,end,index = None):
        if index is None:
            rand = random.randint(begin,end)
            self.exch(num,begin,rand)
        else:
            self.exch(num,begin,index)
        x = num[begin]
        i = begin
        j = begin
        while j <= end:
            if num[j] < x:
                i += 1
                self.exch(num,i,j)
            j += 1
        self.exch(num,i,begin)
        return i

    def exch(self,num,a,b):
        t = num[a]
        num[a] = num[b]
        num[b] = t


if __name__ == '__main__':
    slt = Solution()
    num = [1, 3, 7, 8, 9, 2, 6, 4, 10, 5]
    k = 9
    result = slt.solute(num,k)
    print(num,k,result)
