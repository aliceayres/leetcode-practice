'''
Merge-Sort 归并排序

'''
import math
import sys
class Solution:
    def merge(self,numbers,p,q,r):
        left = numbers[p:q+1]
        right = numbers[q+1:r+1]
        left += [sys.maxsize]
        right += [sys.maxsize]
        i = 0
        j = 0
        for k in range(p,r+1):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1

    def mergeSort(self,numbers,p,r):
        print(numbers)
        print(numbers[p:r+1])
        print(p,r)
        if p < r:
            q = math.floor((p+r)/2)
            print(q)
            self.mergeSort(numbers,p,q)
            self.mergeSort(numbers,q+1,r)
            self.merge(numbers,p,q,r)

if __name__ == '__main__':
    slt = Solution()
    numbers = [1,3,6,8,2,7,12,16]
    print('# Merge sort is:')
    slt.mergeSort(numbers,0,len(numbers)-1)
    print(numbers)