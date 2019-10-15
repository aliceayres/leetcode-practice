'''
kth quantiles K分位数 9.3-6
n个元素集合无序寻找k分位数 k-1个统计量
k分位数 有序k等分(个数相差不超过1)
'''

class Solution:
    def solute(self,num,k):
        return self.quantiles(num,0,len(num)-1,k)

    def quantiles(self,num,begin,end,k):
        if k == 1:
            return [self.select(num,begin,end,end-begin+1)[0]]
        if begin == end:
            return [num[begin]]
        left = k//2
        right = k - left
        bound = int((end-begin+1)/k * left)  # this bound not median !!!
        m,pivot = self.select(num,begin,end,bound)
        self.exch(num,begin,pivot)
        i = begin
        for j in range(begin+1,end+1):
            if num[j] <= m:
                i += 1
                self.exch(num,i,j)
        self.exch(num,i,begin)
        left_quantiles = self.quantiles(num,begin,i,left)
        right_quantiles = self.quantiles(num,i+1,end,right)
        return left_quantiles+right_quantiles

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
    num = [3,1,7,2,4,5,8,6,9,10,11,12]
    k = 5
    result = slt.solute(num,k)
    print(num)
    print(result)     