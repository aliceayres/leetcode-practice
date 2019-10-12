'''
Radix sort 基数排序
桶内保持上一轮顺序
'''


class Solution:
    def solute(self,num,d):
        return self.radix(num,d)

    def radix(self,num,d):
        k = d
        by = 10
        result = num[:]
        while k > 0:
            cache = [[] for i in range(10)]
            for i in range(len(result)):
                c = result[i] % by // (by // 10)
                cache[c].append(result[i])       # keep same c in the same bulket! not like counting sort!
            result = []
            for e in cache:
                while len(e) > 0:
                    result.append(e.pop(0))
            print(result)
            by *= 10
            k -= 1
        return result

if __name__ == '__main__':
    slt = Solution()
    num = [15,224,6,678,2321,627,89,900]
    d = 4
    print("radix sorted :", slt.solute(num,d))