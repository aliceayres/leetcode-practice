'''
Longest Increasinng Subsequence 最长递增子序列
15.4-5 n^2
15.4-6 nlgn
'''
import random

def searchMinLargerIndex(nums,begin,end,x):
    mid = (begin+end)//2
    if nums[mid] < x:
        if mid + 1 > end:
            return mid + 1
        return searchMinLargerIndex(nums,mid+1,end,x)
    elif nums[mid] > x:
        if mid - 1 < begin:
            return mid
        return searchMinLargerIndex(nums,begin,mid-1,x)
    else:
        return mid

class Solution:
    def dp(self,nums):
        ls = [1 for i in range(len(nums))] # ls[i]:以nums[i]尾数的子序列的最大长度
        longest = 1
        idx = 0
        for i in range(len(nums)):  # n^2
            for k in range(i):
                if nums[k] < nums[i]:
                    if ls[i] <= ls[k] + 1:  # = decide behind longest
                        ls[i] = ls[k] + 1
            if ls[i] > longest:
                longest = ls[i]
                idx = i
        print(ls)
        lis = [nums[idx]]
        j = idx - 1
        last_idx = idx
        while len(lis) < longest:
            if nums[j] < lis[0] and ls[j] == ls[last_idx] - 1: # ls
                last_idx = j
                lis = [nums[j]] + lis
            j -= 1
        return lis

    def dpopt(self,nums):
        ls = [] # ls[i]:i长度自序列的最小尾数
        last_idx = -1
        for i in range(len(nums)):
            if len(ls) == 0:
                ls.append(nums[i])
                last_idx = i
            elif nums[i] > ls[-1]:
                ls.append(nums[i])
                last_idx = i
            elif nums[i] < ls[-1]:
                idx = searchMinLargerIndex(ls,0,len(ls)-1,nums[i])
                ls[idx] = nums[i]
        print(ls)
        j = len(ls)-2
        lis = [nums[last_idx]]
        i = last_idx
        while len(lis) < len(ls):
            if ls[j] <= nums[i] < lis[0]:
                lis = [nums[i]] + lis
                j -= 1
            i -= 1
        return lis

def randomNums(n,max):
    return [random.randint(1,max) for i in range(n)]

if __name__ == '__main__':
    slt = Solution()
    nums = randomNums(20,100)
    print(nums)
    r = slt.dp(nums)
    print(r)
    rs = slt.dpopt(nums)
    print(rs)
    st = sorted(nums)
    x = st[5]+0.3
    print(st)
    ix = searchMinLargerIndex(st,0,19,x)
    print(x)
    print(ix)
    print(st[ix])