'''
nlgn 计算逆序对数量
逆序对 : i<j , a[i]>a[j]
'''

import sys

class Solution:
    def solute(self,num):
        nums = num[0:]
        inversion = self.inversion(nums,0,len(nums)-1)
        print(nums)
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
            print(num[begin:mid+1],num[mid+1:end+1],left,right,cross)
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
                cnt += j   #???
            else:
                num[k] = right[j]
                j += 1
        return cnt

if __name__ == '__main__':
    slt = Solution()
    num = [2,9,18,4,9,5,6,12]
    result = slt.solute(num)
    result2 = slt.naive(num)
    print(result)
    print(result2)
    print(num)