'''
Quicksort 快速排序
'''


class Solution:
    def solute(self,num):
        self.quicksort(num,0,len(num)-1)
        return

    def quicksort(self,num,p,r):
        if p < r:
            q = self.partition(num,p,r)
            self.quicksort(num,p,q-1)
            self.quicksort(num,q+1,r)

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
    numbers = [2, 1, 4, 9, 3, 12, 7, 6]
    slt.solute(numbers)
    print(numbers)