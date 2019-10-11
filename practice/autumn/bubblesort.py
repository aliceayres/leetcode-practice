'''
Bubble sort 冒泡排序
'''


class Solution:
    def solute(self,num):
        return self.bubble(num)

    def bubble(self,num):
        l = len(num)
        for i in range(l):
            j = l-1
            while j >= i:
                if num[j] <= num[j-1]:
                    t = num[j]
                    num[j] = num[j-1]
                    num[j-1] = t
                j -= 1
        return num


if __name__ == '__main__':
    slt = Solution()
    k = 10
    num = [2,1,4,9,3,12,7,6]
    print(slt.solute(num) )