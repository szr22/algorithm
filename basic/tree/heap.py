import random
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.curSize = 0

    def percUp(self, i):
        while i//2>0:
            if self.heapList[i] < self.heapList[i//2]:
                # tmp = self.heapList[i//2]
                # self.heapList[i//2] = self.heapList[i]
                # self.heapList[i] = tmp
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2]
            i = i//2

    def insert(self, num):
        self.heapList.append(num)
        self.curSize += 1
        self.percUp(self.curSize)

    def percDown(self, i):
        while (i*2) <= self.curSize:
            mChildIdx = self.minChild(i)
            if self.heapList[i] > self.heapList[mChildIdx]:
                self.heapList[i], self.heapList[mChildIdx] = self.heapList[mChildIdx], self.heapList[i]
            i = mChildIdx

    def minChild(self, i):
        if i*2+1 > self.curSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.curSize]
        self.curSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, arr):
        i = len(arr)//2
        self.curSize = len(arr)
        self.heapList = [0] + arr[:]
        while i>0:
            self.percDown(i)
            i -= 1

def main():
    biHeap = BinaryHeap()
    arr = []
    for i in range(10):
        arr.append(random.randint(1,100))
        # biHeap.insert(random.randint(1,50))
    print(arr)
    # for num in arr:
    #     biHeap.insert(num)
    biHeap.buildHeap(arr)
    print(biHeap.heapList)
    minNum = biHeap.delMin()
    print(biHeap.heapList)

if __name__ == "__main__":
    main()

    