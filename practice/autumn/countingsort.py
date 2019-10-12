'''
Counting sort 计数排序
整数范围0-k
'''


class Solution:
    def solute(self, num,k):
        return self.counting_off(num,k)

    def countingsort(self, num,k):
        cache = [0 for i in range(k+1)]
        result = [0 for i in range(len(num))]
        for e in num:
            cache[e] += 1
        for i in range(1, k+1):
            cache[i] += cache[i-1]
        for e in num:
            idx = cache[e]
            result[idx] = e
            cache[e] -= 1
        return result


    def counting_off(self, num,k):
        cache = [0 for i in range(k+1)]
        result = [0 for i in range(len(num))]
        for e in num:
            cache[e] += 1
        j = 0
        for i in range(len(cache)):
            while cache[i] > 0:
                result[j] = i
                cache[i] -= 1
                j += 1
        return result

if __name__ == '__main__':
    slt = Solution()
    k = 10
    num = [4,5,2,1,0,1,9,5,3,2,10]
    print(slt.solute(num,k) )