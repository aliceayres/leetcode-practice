'''
Kth smallest rank 第k小的值
'''

import random

class Solution:
    def solute(self,num,k):
        return self.exlinear(num,0,len(num)-1,k)

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


    def randpart(self,num,begin,end):
        rand = random.randint(begin,end)
        self.exch(num,begin,rand)
        x = num[begin]
        i = begin
        j = begin
        print(x)
        while j <= end:
            if num[j] < x:
                i += 1
                self.exch(num,i,j)
            j += 1

        self.exch(num,i,begin)
        print(num[begin:end+1])
        return i

    def exch(self,num,a,b):
        t = num[a]
        num[a] = num[b]
        num[b] = t


if __name__ == '__main__':
    slt = Solution()
    num = [1, 3, 9, 2, 6, 4, 5, 7, 8, 10]
    k = 10
    result = slt.solute(num,7)
    print(result)