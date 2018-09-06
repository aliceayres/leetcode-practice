'''
7. 斐波那契数列
题目描述：
求斐波那契数列的第 n 项，n <= 39。
'''

class Solution:
    def fibonacci(self, n):
        if n <= 2:
            return 1
        return self.fibonacci(n-1)+self.fibonacci(n-2)

    def fibonacciStore(self, n):
        if n <= 2:
            return 1
        store1 = 1
        store2 = 2
        for i in range(3, n-1):
            current = store1 + store2
            store1 = store2
            store2 = current
        return store1+store2


slt = Solution()
n = 10
print(slt.fibonacci(n))
print(slt.fibonacciStore(n))
