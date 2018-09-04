'''
2.1 插入排序
Insertion Sort
T = o(n2)
'''

class Solution:
    def insertionSort(self, numbers):
        """
        :type numbers: List[int] 直接处理原数组
        """
        for i in range(len(numbers)-1):
            current = numbers[i]
            j = i - 1
            while j >= 0 and current < numbers[j]:
                numbers[j+1] = numbers[j]
                j -= 1
            numbers[j+1] = current

if __name__ == '__main__':
    slt = Solution()
    numbers = [2,1,4,9,3,12]
    print('# Insertion sort is:')
    slt.insertionSort(numbers)
    print(numbers)