import heapq

class MaxHeapObj(object):
    def __init__(self,val): self.val = val
    def __str__(self): return str(self.val)
    def __lt__(self, other):
        if self.val[1] < other.val[1]:
            return True
        elif self.val[1] > other.val[1]:
            return False
        else:
            return self.val[0] > other.val[0]


class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self,x): heapq.heappush(self.h,x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
    def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self,i): return self.h[i].val


minh = MinHeap()
maxh = MaxHeap()
# add some values
minh.heappush((12, 'a'))
minh.heappush((12, 'aa'))
maxh.heappush((12, 'aa'))
maxh.heappush((12, 'a'))
minh.heappush((4, 'b'))
maxh.heappush((4, 'b'))
# fetch "top" values
print(minh[0],maxh[0]) # "4 12"
# fetch and remove "top" values
print(minh.heappop(),maxh.heappop()) # "4 12"


import sys

class MinHeap2:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0 for _ in range(self.maxsize+1)]
        self.heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return 2 * pos + 1

    def isLeaf(self, pos):
        if pos >= self.size//2 and pos <= self.size:
            return True
        return False

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (
                self.heap[pos] > self.heap[self.leftChild(pos)]
                or self.heap[pos] > self.heap[self.rightChild(pos)]
            ):
                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, elem):
        if self.size > self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = elem

        cur = self.size
        while self.heap[cur] < self.heap[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    def remove(self):
        removed = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return removed

    def __str__(self):

        res = ''
        for i in range(1, self.size//2+1):
            res += (
                " PARENT : " + str(self.heap[i])
                + " LEFT CHILD : " + str(self.heap[2 * i])
                + " RIGHT CHILD : " + str(self.heap[2 * i + 1])
                + "\n"
            )
        return res

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)


if __name__ == "__main__":

    print('The minHeap is ')
    minHeap = MinHeap2(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    print(minHeap)
    print("The Min val is " + str(minHeap.remove()))