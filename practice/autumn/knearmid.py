'''
Kth near median
最接近中位数的K个数 n
'''
import random

class Solution:
    def solute(self,num,k):
        return self.knearmid(num,k)

    def knearmid(self,num,k):
        mid = len(num)//2+1
        median_tuple = self.select(num,0,len(num)-1,mid)
        median = median_tuple[0]
        print(median)
        cache = []
        map = {}
        for i in range(len(num)):
            d = abs(num[i]-median)
            if map.get(d) is not None:
                tail = random.randint(1,100)/1000 # prevent distance same
                d = d + tail
            cache.append(d)
            map[d] = i
            print(num[i],d)
        print(num)
        print(cache)
        distance_tuple = self.select(cache[:],0,len(cache)-1,k+1)
        distance = distance_tuple[0]
        result = []
        for i in range(len(cache)):
            if cache[i] <= distance and cache[i] != 0:
                result.append(num[map.get(cache[i])])
        return result

    def select(self,num,begin,end,k):
        if begin == end:
            return num[begin],begin
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
        x,index = self.select(mids,0,len(mids)-1,k_mid)
        index = cache[x]
        pivot = self.partition(num,begin,end,index)
        if k == pivot+1-begin:    # don't forget begin
            return num[pivot],pivot
        elif k < pivot+1-begin:
            return self.select(num,begin,pivot-1,k)
        else:
            return self.select(num,pivot+1,end,k-pivot-1+begin)

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

    def partition(self,num,begin,end,index):
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
    num = [1,2,3,4,5,6,7,8,9]
    result = slt.solute(num,5)
    print(result)     