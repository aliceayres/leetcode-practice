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
                print('&&&')
                break;
            if p > len(search)-1:
                median = other[q]
                median2 = other[q + 1]
                break;
            if q > len(other)-1:
                median = search[p]
                median2 = search[p + 1]
                break;
            if p+1 > len(search)-1:
                median = max(search[p], other[q])
                median2 = other[q + 1]
                break;
            if q+1 > len(other)-1:
                median = max(search[p], other[q])
                median2 = search[p+1]
                break;
            if p < 0:
                median = other[q]
                median2 = min(search[p + 1], other[q + 1])
                break;
            if q < 0:
                median = search[p]
                median2 = min(search[p + 1], other[q + 1])
                break;
            if search[p] <= other[q+1] and other[q] <= search[p+1]:
                median = max(search[p], other[q])
                median2 = min(search[p + 1], other[q + 1])
                break;
            if search[p] > other[q+1]: # left search
                end = p -1
            if other[q] > search[p+1]: # right search
                start = p + 1
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
    a = [4,5]
    b = [1,2,3,6]
    s = Solution()
    median = s.findMedianSortedArrays(b,a)
    median2 = s.findMedianSortedArrays(b,a)
    print(median)
    print(median2)