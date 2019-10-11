'''
Selection sort 选择排序 2.2-2
'''


class Solution:
    def solute(self,num):
        return self.selection(num)

    def selection(self,num):
        for i in range(len(num)):
            for j in range(i,len(num)):
                if num[j] <= num[i]:
                    t = num[i]
                    num[i] = num[j]
                    num[j] = t
        return num


if __name__ == '__main__':
    slt = Solution()
    k = 10
    num = [4,5,2,1,0,1,9,5,3,2,10]
    print(slt.solute(num) )