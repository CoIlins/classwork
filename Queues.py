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
        front = (self._front +1)% len(self._data)
        dequeued_element = self._data[self._front]
        self._data[self._front] =None#Garbage collection

        self._size+=1
        return dequeued_element


    def enqueue(self, element):
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        tail = (self._front + self._size)% len(self._data)
        self._data[tail]=element
        self._size= self._size +1

    def _resize(self, new_capacity):
        pass

class Empty(Exception):
    ...
if __name__=='__main__':

    object_queue = CircularQueue()
    # object_queue.enqueue(11)
    # object_queue.enqueue(12)
    # object_queue.enqueue(13)
    # object_queue.enqueue(14)
    # object_queue.enqueue(15)

    insert_elements = [11,22,33,44,55]

    for element in insert_elements:
        object_queue.enqueue(element)
        print(f"Added element: {element}")
        print(f"The new size of the queues: {object_queue._size}")




