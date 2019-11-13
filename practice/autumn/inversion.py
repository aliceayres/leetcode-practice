'''
nlgn 计算逆序对数量
逆序对 : i<j , a[i]>a[j]
14.1-7 ost 逆序对
'''

import sys
from practice.autumn.rbtreesubcnt import RBTree as ost

class Solution:
    def solute(self,num):
        nums = num[0:]
        inversion = self.inversion(nums,0,len(nums)-1)
        return inversion

    def ostree(self,num):
        tree = ost()
        inversion = 0
        for e in num:
            tree.rb_insert(e)
            rank = tree.os_rank(e)
            inversion += (tree.root.size - rank)
        return inversion

    def naive(self,num):
        sum = 0
        for i in range(len(num)):
            for j in range(len(num)):
                if i < j and num[i] > num[j]:
                    sum += 1
        return sum

    def inversion(self,num,begin,end):
        if begin < end:
            mid = (begin+end)//2
            left = self.inversion(num,begin,mid)
            right = self.inversion(num,mid+1,end)
            cross = self.mergecross(num,begin,end)
            return left + right + cross
        else:
            return 0

    def mergecross(self,num,begin,end):
        mid = (begin + end) // 2
        left = num[begin:mid+1]+[sys.maxsize]
        right = num[mid+1:end+1]+[sys.maxsize]
        i = 0
        j = 0
        cnt = 0
        for k in range(begin,end+1):
            if left[i] <= right[j]:
                num[k] = left[i]
                i += 1
                cnt += j  # j为right中之前比left[i]小的数的数量
            else:
                num[k] = right[j]
                j += 1
        return cnt

if __name__ == '__main__':
    slt = Solution()
    num = [2,9,18,4,9,5,6,12]
    r1 = slt.solute(num)
    r2 = slt.naive(num)
    r3 = slt.ostree(num)
    print(num)
    print(r1)
    print(r2)
    print(r3)
