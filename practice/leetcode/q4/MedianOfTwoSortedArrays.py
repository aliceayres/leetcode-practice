"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        odd = (m + n) % 2 == 1
        number = []
        if len(nums1) == 0 and len(nums2) == 0: # special situation
            return 0.0
        if len(nums1) == 0:
            number = nums2
        elif len(nums2) == 0:
            number = nums1
        elif nums1[-1] < nums2[0]:  # straightly extend
            number.extend(nums1)
            number.extend(nums2)
        elif nums2[-1] < nums1[0]:
            number.extend(nums2)
            number.extend(nums1)
        if len(number) != 0:
            index = len(number) // 2
            if odd:
                return number[index] / 1.0
            else:
                return (number[index] + number[index - 1]) * 1.0 / 2
# normal situation
        k = (m + n + 1) // 2
        search = nums1
        other = nums2
        end = m - 1
        start = 0
        if m > n:
            search = nums2
            other = nums1
            t = n
        while True:
            p = (end + start) // 2
            q = k - p - 2
            if start > end:
                break;
            ls = -1 if p < 0 else search[p]
            lo = -1 if q < 0 else other[q]
            rs = 1000000 if p >= len(search)-1 else search[p+1]
            ro = 1000000 if q >= len(other)-1 else other[q+1]
            if ls <= ro and lo <=rs:
                break;
            if ls > ro: # left search
                end = p -1
            if lo > rs: # right search
                start = p + 1
        median = max(ls, lo)
        median2 = min(rs, ro)
        if odd:
            return 2 * median / 2.0
        else:
            return (median + median2) / 2.0

    def findMedianSortedArraysNotLogMN(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1)+len(nums2)
        odd = length % 2 == 1
        index = (length + 1)//2-1
        number = []
        i = 0
        j = 0
        if len(nums1) == 0 and len(nums2) == 0: # special situation
            return 0.0
        if len(nums1) == 0:
            number = nums2
        elif len(nums2) == 0:
            number = nums1
        elif nums1[-1] < nums2[0]:  # straightly extend
            number.extend(nums1)
            number.extend(nums2)
        elif nums2[-1] < nums1[0]:
            number.extend(nums2)
            number.extend(nums1)
        else:
            while True:
                # if i > len(nums1)-1 and j > len(nums2)-1:
                if len(number) > index + 2: # not require to all numbers
                    break
                if i > len(nums1) - 1:
                    number.extend(nums2[j:])
                    break
                if j > len(nums2) - 1:
                    number.extend(nums1[i:])
                    break
                if nums1[i] <= nums2[j]:
                    number.append(nums1[i])
                    i = i + 1
                else:
                    number.append(nums2[j])
                    j = j + 1
        if odd:
            return number[index]/1.0
        else:
            return (number[index]+number[index+1])*1.0/2

if __name__ == '__main__':
    a = [1,3,4]
    b = [2]
    s = Solution()
    median = s.findMedianSortedArrays(b,a)
    median2 = s.findMedianSortedArrays(b,a)
    print(median)
    print(median2)