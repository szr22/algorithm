class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = 0
        self.arr = [0 for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[(self.head+self.size)%self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head+1)%self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.head+self.size-1)%self.capacity]


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def print_queue(self):
        print(self.arr)

my_circular_queue = MyCircularQueue(3)
my_circular_queue.enQueue(1)
my_circular_queue.print_queue()
my_circular_queue.enQueue(2)
my_circular_queue.print_queue()
my_circular_queue.enQueue(3)
my_circular_queue.print_queue()
my_circular_queue.enQueue(4)
my_circular_queue.print_queue()
my_circular_queue.Rear()
my_circular_queue.print_queue()
my_circular_queue.isFull()
my_circular_queue.print_queue()
my_circular_queue.deQueue()
my_circular_queue.print_queue()
my_circular_queue.enQueue(4)
my_circular_queue.print_queue()
print(my_circular_queue.Rear())
my_circular_queue.print_queue()
print(my_circular_queue.Front())
my_circular_queue.print_queue()