'''
2.3-7
排序 nlgn
有序数组查找是否存在两数之和x
二分 nlgn
线性 n
'''

class Solution:
    def solute(self,num,x):
        return self.linear(num,x)

    def linear(self,num,x):
        i = 0
        j = len(num)-1
        while i < j:
            if num[i]+num[j] == x:
                return num[i],num[j]
            elif num[i]+num[j] < x:
                i += 1
            else:
                j -= 1
        return None

if __name__ == '__main__':
    slt = Solution()
    num = [1, 2, 3, 14, 16, 17, 19, 22]
    x = 30
    result = slt.solute(num,x)
    print(result)     