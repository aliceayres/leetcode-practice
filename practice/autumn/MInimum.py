'''
Minimum 最小值
同时求最大值和最小值
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

    def double(self,num):
        if len(num) == 0:
            return None
        min = num[0]
        max = num[0]
        i = 0
        while i < len(num):
            if i + 1 < len(num):
                if num[i] <= num[i+1]:
                    if num[i] < min:
                        min = num[i]
                    if num[i+1] > max:
                        max = num[i+1]
                else:
                    if num[i+1] < min:
                        min = num[i+1]
                    if num[i] > max:
                        max = num[i]
            else:
                if num[i] < min:
                    min = num[i]
                if num[i] > max:
                    max = num[i]
            i += 2
        return min,max

if __name__ == '__main__':
    slt = Solution()
    num = [1,6,22,9,-13,0,2,1,89]
    result = slt.solute(num)
    print(result)
    print(slt.double(num))