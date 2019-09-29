'''
Binary search 二分查找
'''


class Solution:
    def solute(self,num,x):
        return self.binarysearch(num,0,len(num)-1,x)

    def binarysearch(self,num,p,q,x):
        if p > q:
            return -1
        mid = (p+q)//2
        if num[mid] == x:
            return mid
        elif num[mid] > x:
            return self.binarysearch(num,p,mid - 1,x)
        else:
            return self.binarysearch(num, mid + 1,q , x)


if __name__ == '__main__':
    slt = Solution()
    num = [1,5,9,11,14,45,80]
    target = 87
    idx = slt.solute(num,target)
    print(idx)