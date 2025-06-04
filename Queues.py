class CircularQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY#_ means the variable is sensitive
        self._size = 0
        self._front= 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')#raise is like a return .It will return a value
        return self._data[self._front]


    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty for dequeue operation')



    def enqueue(self):
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        tail = (self._front * self._size)% len(self._data)

    def _resize(self, new_capacity):
        pass

class Empty(Exception):
    ...
if __name__=='__main__':

    object_queue = Circular