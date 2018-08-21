'''
4.1 最大子数组问题
Maximum Subsequence Sum
分治策略
T = o(nlgn)
'''

class Solution:
    def maximumSubsequenceSum(self, original):
        """
        :type numbers: List[int]
        :rtype: int,int,int
        """
        return self.maxSum(0,len(original)-1,original)

    def maxSum(self, left, right, original):
        if len(original) == 0:
            return 0,0,0
        if left == right:
            return left,right,original[left]
        else:
            mid = int((left + right) / 2)
            l_left,l_right,l_sum = self.maxSum(left,mid,original)
            r_left,r_right,r_sum = self.maxSum(mid+1,right,original)
            c_left,c_right,c_sum = self.crossMaxSum(left,right,original,mid)
            max_sum = max(l_sum, r_sum, c_sum)
            if max_sum==l_sum:
                return l_left,l_right,l_sum
            if max_sum==r_sum:
                return r_left,r_right,r_sum
            if max_sum==c_sum:
                return c_left,c_right,c_sum

    def crossMaxSum(self, left, right, original, mid):
        left_sum = original[mid]
        left_max = original[mid]
        left_left = mid
        i = mid-1
        while i >= left:
            left_sum = left_sum + original[i]
            if left_sum >= left_max:
                left_max = left_sum
                left_left = i
            i = i-1
        right_sum = original[mid+1]
        right_max = original[mid+1]
        right_right = mid+1
        j = mid+2
        while j <= right:
            right_sum = right_sum + original[j]
            if right_sum >= right_max:
                right_max = right_sum
                right_right = j
            j = j+1
        return left_left,right_right,left_max+right_max

if __name__ == '__main__':
    slt = Solution()
    numbers = [13,-3,-25,20,-3,-16,-23,-5,-22,15,18,20,-7,12,-4,7]
    print('# maximum subsequence sum is:')
    print(slt.maximumSubsequenceSum(numbers))