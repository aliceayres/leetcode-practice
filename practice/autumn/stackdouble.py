'''
Double Stack 双栈 10.1-2
'''


class Stack:
    def __init__(self,size):
        self.stack = [None for i in range(size)]
        self.ltop = -1
        self.rtop = size
        self.size = size

    def lpush(self,x):
        if self.ltop + 1 == self.rtop:
            raise Exception('left stack upflow')
        self.ltop += 1
        self.stack[self.ltop] = x

    def lpop(self):
        if self.ltop == -1:
            raise Exception("left stack underflow")
        e = self.stack[self.ltop]
        self.stack[self.ltop] = None
        self.ltop -= 1
        return e

    def rpush(self,x):
        if self.rtop - 1 == self.ltop:
            raise Exception('right stack upflow')
        self.rtop -= 1
        self.stack[self.rtop] = x

    def rpop(self):
        if self.rtop == self.size:
            raise Exception("right stack underflow")
        e = self.stack[self.rtop]
        self.stack[self.rtop] = None
        self.rtop += 1
        return e

if __name__ == '__main__':
    stack = Stack(10)
    num = ["e","b","a","c","d","f","h"]
    for e in num:
        stack.lpush(e)
    stack.rpush("c")
    stack.rpush("d")
    stack.rpush("z")
    print(stack.stack)
    print(stack.lpop())
    print(stack.lpop())
    print(stack.lpop())
    print(stack.rpop())
    print(stack.stack)