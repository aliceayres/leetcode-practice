'''
1. 数组中重复的数字
题目描述:
在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重
复的，但不知道有几个数字是重复的，也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
要求：
时间复杂度 o(N), 空间复杂度 o(1)
'''

class Solution:
    def anyRepeatedNumber(self,numbers):
        for e in numbers:
            if numbers[e] < 0:
                return e
            if numbers[e] > 0:
                numbers[e] *= -1
            else:
                numbers[e] = -len(numbers)
        return

slt = Solution()
repeated = slt.anyRepeatedNumber(numbers=[0,1,0,2,3,1,4])
print(repeated)