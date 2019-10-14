'''
Minimum 最小值
'''


class Solution:
    def solute(self,num):
        if len(num) == 0:
            return None
        mini = num[0]
        for e in num:
            if e < mini:
                mini = e
        return mini


if __name__ == '__main__':
    slt = Solution()
    num = [1,6,22,9,-13,0,2,1]
    result = slt.solute(num)
    print(result)     