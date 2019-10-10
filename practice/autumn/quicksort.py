'''
Quicksort 快速排序
'''
import random

class Solution:
    def solute(self,num):
        self.randquicksort(num,0,len(num)-1)
        return

    def quicksort(self,num,p,r):
        if p < r:
            q = self.partition(num,p,r)
            self.quicksort(num,p,q-1)
            self.quicksort(num,q+1,r)


    def randquicksort(self,num,p,r):
        if p < r:
            q = self.randomp(num,p,r)
            self.randquicksort(num,p,q-1)
            self.randquicksort(num,q+1,r)

    def randomp(self,num,p,r):
        idx = random.randint(p,r)
        self.exchange(num,p,idx)
        x = num[p]
        i = p
        for j in range(p+1,r+1):
            if num[j] <= x:
                i = i + 1
                self.exchange(num,i,j)
        self.exchange(num,p,i)
        return i

    def partition(self,num,p,q):
        x = num[p]
        i = p
        for j in range(p+1,q+1):
            if num[j] <= x:
                i += 1
                self.exchange(num,i,j)
        self.exchange(num,p,i)
        return i

    def exchange(self,num,x,y):
        t = num[x]
        num[x] = num[y]
        num[y] = t

if __name__ == '__main__':
    slt = Solution()
    numbers = [1, 2, 4, 9, 11, 12, 17, 26]
    slt.solute(numbers)
    print(numbers)