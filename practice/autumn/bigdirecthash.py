'''
11.1-4 大数组直接寻址表
'''
class Data:
    def __init__(self,key,data):
        self.key = key
        self.data = data

    def __str__(self):
        return format('key=%d,data=%s' % (self.key,self.data))

class AdditionalStack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def stack_empty(self):
        return self.top == -1

    def push(self,x):
        self.top += 1
        self.stack.append(x)
        return self.top

    def pop(self):
        if self.stack_empty():
            raise Exception("stack underflow")
        e = self.stack.pop(self.top)
        self.top -= 1
        return e

    def get(self,index):
        if index is not None and 0 <= index <= self.top:
            return self.stack[index]
        return None

    def delete(self,index):
        if index is not None and 0 <= index <= self.top:
            t = self.stack[self.top]
            self.stack[self.top] = self.stack[index]
            self.stack[index] = t
            self.pop()
            return t.key
        return None

class BigDirectHash:
    def __init__(self):
        self.hash = [i for i in range(10000,20000)]
        self.stack = AdditionalStack()

    def search(self,key):
        index = self.hash[key]
        data = self.stack.get(index)
        if data is not None and data.key == key:
            return data
        return None

    def insert(self,data):
        index = self.stack.push(data)
        self.hash[data.key] = index
        return

    def delete(self,key):
        index = self.hash[key]
        key = self.stack.delete(index)
        if key is not None:
            self.hash[key] = index
        return

if __name__ == '__main__':
    hash = BigDirectHash()
    d1 = Data(3789,'hello')
    d2 = Data(9365,'world')
    hash.insert(d2)
    hash.insert(d1)
    print(hash.search(3789))
    print(hash.search(9365))
    print(hash.search(1759))
    hash.delete(9365)
    print(hash.search(9365))
    hash.delete(1345)
    print(hash.search(3789))