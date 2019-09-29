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

    def merge2(self,numbers,p,q,r):
        left = numbers[p:q + 1]
        right = numbers[q + 1:r + 1]
        i = 0
        j = 0
        for k in range(p, r + 1):
            if j >= len(right) and i < len(left):
                numbers[k] = left[i]
                i += 1
            elif i>= len(left) and j < len(right):
                numbers[k] = right[j]
                j += 1
            elif left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1

    def mergeSort(self,numbers,p,r):
        if p < r:
            q = math.floor((p+r)/2)
            self.mergeSort(numbers,p,q)
            self.mergeSort(numbers,q+1,r)
            self.merge2(numbers,p,q,r)

if __name__ == '__main__':
    slt = Solution()
    numbers = [2,1,4,9,3,12,7,6]
    slt.mergeSort(numbers,0,len(numbers)-1)
    print(numbers)