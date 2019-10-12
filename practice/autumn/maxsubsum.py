'''
Maximum Subsequence Sum 最大子数组和
naive 暴力求解 n^2 4.1-2
subseq 递归解法 nlgn
linear 线性时间解法 n 4.1-5
'''


class Solution:
    def solute(self,num):
        # return self.linear(num,0,len(num)-1)
        return self.naive(num)


    def naive(self,num):
        max = num[0]
        begin = 0
        end = 0
        for i in range(len(num)):
            sum = 0
            for j in range(i,len(num)):
                sum += num[j]
                if sum > max:
                    max = sum
                    begin = i
                    end = j
        return max,begin,end


    def subseq(self,num,begin,end):
        if len(num) == 0:
            return 0,0,0
        if begin < end :
            mid = (begin+end)//2
            ls,ll,lr = self.subseq(num,begin,mid)
            rs,rl,rr = self.subseq(num,mid+1,end)
            cs,cl,cr = self.cross(num,begin,end)
            if ls >= rs and ls >= cs:
                return ls,ll,lr
            if rs >= ls and rs >= cs:
                return rs,rl,rr
            if cs >= rs and cs >= ls:
                return cs,cl,cr
        else:
            return num[begin],begin,begin

    def cross(self,num,begin,end):
        mid = (begin + end) // 2
        sum = 0

        left = mid
        right = mid+1
        left_max = num[left]
        right_max = num[right]
        idx = mid
        while idx > begin:
            sum += num[idx]
            if sum > left_max:
                left_max = sum
                left = idx
            idx -= 1
        idx = mid + 1
        sum = 0
        while idx <= end:
            sum += num[idx]
            if sum > right_max:
                right_max = sum
                right = idx
            idx += 1
        return left_max+right_max,left,right

    def linear(self, num, begin, end):
        last_max = num[begin]
        last_left = begin
        last_right = begin
        sub = num[begin]
        sub_left = begin
        for i in range(begin + 1, end + 1):
           if sub+num[i] > num[i]:
                sub += num[i]
           else:
                sub = num[i]
                sub_left = i
           if last_max <= sub:
                last_max = sub
                last_left = sub_left
                last_right = i
        return last_max, last_left, last_right

    def linear_off(self,num,begin,end):
        last_max = num[begin]
        last_left = begin
        last_right = begin
        for j in range(begin+1,end+1):
            idx = j
            left = j
            max = num[idx]
            sum = 0
            while idx >= 0:
                sum += num[idx]
                if sum > max:
                    max = sum
                    left = idx
                idx -= 1
            if max >= last_max:
                last_max = max
                last_left = left
                last_right = j
        return last_max,last_left,last_right

if __name__ == '__main__':
    slt = Solution()
    num = [13,-3,-25,20,-3,-16,-23,-5,-22,15,18,20,-7,12,-4,7]
    print(slt.solute(num))