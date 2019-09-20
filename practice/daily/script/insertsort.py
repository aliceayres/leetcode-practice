'''
Insertion-Sort 插入排序

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

if __name__ == '__main__':
    slt = Solution()
    numbers = [2,1,4,9,3,12,7,6]
    print('# Insertion sort is:')
    slt.insertionSort(numbers)
    print(numbers)