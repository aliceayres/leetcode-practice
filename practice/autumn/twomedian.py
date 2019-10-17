'''
Two sorted median
两个n元素的有序数组的中位数 9.3-8
两个不同元素有序数组的K位数 todo
'''


class Solution:
    def solute(self,a,b):
        return self.twomid(a,b)

    def twomid(self,a,b):
        print(a,b)
        mas = (len(a)-1)//2
        mal = len(a) // 2
        mbs = (len(b)-1)//2
        mbl = len(b) // 2
        amid = (a[mas] + a[mal]) / 2
        bmid = (b[mbs] + b[mbl]) / 2
        if len(a)%2 == 1 and amid == bmid: # odd return mid
            return a[mas]
        elif (len(a)%2 == 0 and amid == bmid) or len(a) == 2: # even return larger small mid
            if a[mas] >= b[mas]:
                return a[mas]
            else:
                return b[mas]
        if amid < bmid:
            return self.twomid(a[mas:],b[:mbl+1])
        else:
            return self.twomid(a[:mal+1],b[mbs:])

if __name__ == '__main__':
    slt = Solution()
    a = [1,3,5,7,9]
    b = [2,4,8,10,11]
    result = slt.solute(a,b)
    print(result)     