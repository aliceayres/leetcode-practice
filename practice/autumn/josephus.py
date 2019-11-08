'''
14-2 Josephus排列 约瑟夫环
'''

class Solution:
    def josephus_n(self,n,m):
        num = [i for i in range(1,n+1)]
        josephus = []
        cnt = 0
        i = 0
        while len(josephus) < n:
            if num[i] != 0:
                cnt += 1
            if cnt == m:
                josephus.append(num[i])
                num[i] = 0
                cnt = 0
            i = (i+1) % n
        return josephus

    def josephus_nlgn(selfn,m):
        return

if __name__ == '__main__':
    slt = Solution()
    result = slt.josephus_n(7,3)
    print(result)     