'''
Kth smallest rank 第k小的值
堆排序 归并排序 nlgn
期望线性时间 所有元素互异 n 最坏 n^2 按余下元素中最大的划分
最坏线性时间 n
基于循环 9.2-3
'''

import random

class Solution:
    def solute(self,num,k):
        return self.exlinear_loop(num,0,len(num)-1,k)

    def exlinear(self,num,begin,end,k):
        print(num[begin:end + 1],k)
        if begin == end:
            return num[begin]
        pivot = self.randpart(num,begin,end)
        if k == pivot+1-begin:    # don't forget begin
            return num[pivot]
        elif k < pivot+1-begin:
            return self.exlinear(num,begin,pivot-1,k)
        else:
            return self.exlinear(num,pivot+1,end,k-pivot-1+begin)


    def exlinear_loop(self,num,p,q,r):
        begin = p
        end = q
        kk = r
        while True:
            print(num[begin:end + 1], kk)
            if begin == end:
                return num[begin]
            pivot = self.randpart(num, begin, end)
            if kk == pivot + 1 - begin:  # don't forget begin
                return num[pivot]
            elif kk < pivot + 1 - begin:
                end = pivot - 1
            else:
                kk = kk - pivot - 1 + begin  # here begin will change , calculate new kk first!
                begin = pivot + 1


    def randpart(self,num,begin,end):
        print(begin,end)
        rand = random.randint(begin,end)
        self.exch(num,begin,rand)
        x = num[begin]
        print(x)
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
    num = [1, 3, 9, 2, 6, 4, 5, 7, 8, 10]
    k = 5
    result = slt.solute(num,k)
    print(result)