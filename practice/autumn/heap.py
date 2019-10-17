'''
Heap 堆
堆性质
维护堆性质
建堆
堆排序
'''

class Heap:
    def heap_sort(self,num): # nlgn
        self.build_heap(num)
        i = len(num) - 1 # i is tail index
        while i >= 1:
            self.exch(num,0,i)
            self.max_heapify(num,0,i) # new length = i+1 -1 = i
            i -= 1

    def build_heap(self,num): # not nlgn but n
        i = self.leafbegin(len(num)) - 1
        while i >= 0:
            self.max_heapify(num,i)
            i -= 1
        return num

    def max_heapify(self,num,i,length = None): # lgh
        if length is None:
            length = len(num)
        largest = i
        l = self.left(i)
        r = self.right(i)
        if l < length and num[l] >= num[i]:
            largest = l
        if r < length and num[r] >= num[largest]:  # this compare large and r!
            largest = r
        if largest != i:
            self.exch(num,largest,i)
            self.max_heapify(num,largest,length)

    def max_heapify_loop(self,num,index):
        i = index
        largest = i
        while True:
            l = self.left(i)
            r = self.right(i)
            if l < len(num) and num[l] >= num[i]:
                largest = l
            if r < len(num) and num[r] >= num[largest]:
                largest = r
            if largest != i:
                self.exch(num, largest, i)
                i = largest
            else:
                break

    def exch(self, num, a, b):
        t = num[a]
        num[a] = num[b]
        num[b] = t

    def parent(self,i):
        # return (i-1)>>1
        return (i-1)//2

    def left(self,i):
        # return (i<<1)+1
        return 2*i+1

    def right(self,i):
        # return (i+1)<<1
        return 2*i+2

    def leafbegin(self,n):
        return n//2

if __name__ == '__main__':
    slt = Heap()
    numbers = [4,1,3,2,16,9,10,14,8,7]
    slt.heap_sort(numbers)
    print(numbers)
    # slt.build_heap(numbers)
    # print(numbers)
    # i = 1
    # print(slt.parent(i),i,slt.left(i),slt.right(i))
    # print(slt.leafbegin(12))
    # print(slt.max_heapify_loop(numbers,i))
    # print(numbers)


