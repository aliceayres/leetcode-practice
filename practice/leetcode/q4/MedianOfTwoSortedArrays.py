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
        while True:
            if i > len(nums1)-1 and j > len(nums2)-1:
            # if len(number) > index + 2: # not require to all numbers
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
        print(number[:])
        if odd:
            return number[index]/1.0
        else:
            return (number[index]+number[index+1])*1.0/2

if __name__ == '__main__':
    a = [8,9,13,17,19,45,91]
    b = [1,5,16,18,32]
    s = Solution()
    median = s.findMedianSortedArraysNotLogMN(a,b)
    print(median)