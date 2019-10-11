'''
N位二进制加法 2.1-4
'''


class Solution:
    def solute(self,a,b):
        return self.biplus(a,b)

    def biplus(self,a,b):
        c = [0 for i in range(len(a)+1)]
        last = 0
        for j in range(len(a)):
            i = len(a) - 1 - j
            c[i+1] = (a[i] + b[i] + last) % 2
            last = (a[i] + b[i] + last) // 2
        c[0] = last
        return c

if __name__ == '__main__':
    a = [1,0,0,1]
    b = [1,1,1,1]
    slt = Solution()
    print(slt.solute(a,b))