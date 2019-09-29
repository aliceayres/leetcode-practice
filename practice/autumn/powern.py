'''
x^n powering n
'''


class Solution:
    def solute(self,x,n):
        return self.power(x,n)

    def naive(self,x,n):
        power = 1
        for i in range(n):
            power *= x
        return power

    def power(self,x,n):
        if n == 1:
            return x
        if self.isOdd(n):
            nt = (n - 1) // 2
            root = self.power(x,nt)
            return root*root*x
        else:
            nt = n // 2
            root = self.power(x, nt)
            return root*root

    def isOdd(self,n):
        return n%2 == 1


if __name__ == '__main__':
    slt = Solution()
    x = 27
    n = 50
    power = slt.solute(x,n)
    print(power)