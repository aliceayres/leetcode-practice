class SortSolution:
    def insertationSort(self,nums):
        i = 1
        while i < len(nums):
            j = i - 1
            current = nums[i]
            while j >= 0 and nums[j] > current:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = current
            i += 1

if __name__ == '__main__':
    slt = SortSolution()
    nums = [3,4,1,7,9,2,5,8,0,6]
    slt.insertationSort(nums)
    print(nums)