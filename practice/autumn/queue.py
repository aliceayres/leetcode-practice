'''
Queue 队列
'''


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,x):
        self.stack.append(x)
        return

    def dequeue(self):
        return self.stack.pop(0)


if __name__ == '__main__':
    q = Queue()
    num = ["a","b","c","d","e","f","g","h"]
    for e in num:
        q.enqueue(e)
    for i in range(len(num)+1):
        print(q.dequeue())