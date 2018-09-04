'''
2. 二维数组中的查找
题目描述:
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到
下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断
数组中是否含有该整数
要求：
时间复杂度 o(M+N), 空间复杂度 o(1)
'''

class Solution:
    def matrixSearch(self, numbers, target):
        if numbers is None or len(numbers) == 0 or len(numbers[0]) == 0:
            return False
        i = 0
        j = len(numbers[0])-1
        while i < len(numbers) and j > 0:
            if numbers[i][j] < target:
                i += 1
            elif numbers[i][j] > target:
                j -= 1
            else:
                print('Exist number [%d], position is (%d,%d).' % (target, i, j))
                return True
        return False

slt = Solution()
numbers = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
exist = slt.matrixSearch(numbers, 19)
print(exist)