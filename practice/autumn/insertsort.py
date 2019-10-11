'''
Insertion-Sort 插入排序
二分查找插入位置 2.3-6
'''

class Solution:
    def insertionSort(self,numbers):
        for i in range(1,len(numbers)):
            n = numbers[i]
            j = i - 1
            while(j >= 0 and numbers[j] > n):
                numbers[j+1] = numbers[j]
                j -= 1
            numbers[j+1] = n

    def binsertion(self,num):
        for i in range(1,len(num)):
            n = num[i]
            k = self.binary(num,i)
            j = i
            while j >= k:
                num[j] = num[j-1]
                j -= 1
            num[k] = n

    def binary(self,num,i):
        return self.binarysearch(num,0,i-1,num[i])

    def binarysearch(self,num,begin,end,x):
        if begin > end:
            return None
        mid = (begin + end) // 2
        if num[mid] == x:
            return mid + 1 # that index+1 : mid + 1
        elif num[mid] < x:
            k = self.binarysearch(num, mid + 1, end, x)
            if k is None:
                return mid + 1 # right part begin : mid + 1
            else:
                return k
        else:
            k = self.binarysearch(num, begin, mid-1, x)
            if k is None:
                return mid # left part end+1 : mid - 1 + 1 = mid
            else:
                return k


if __name__ == '__main__':
    slt = Solution()
    numbers = [2,1,4,9,3,12,7,6]
    # slt.insertionSort(numbers)
    slt.binsertion(numbers)
    print(numbers)