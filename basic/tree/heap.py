import random
class MinBinaryHeap:
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
        # add to the end
        self.heapList.append(num)
        self.curSize += 1
        # mode new val to up
        self.percUp(self.curSize)

    def percDown(self, i):
        while (i*2) <= self.curSize:
            # get smaller child's index
            mChildIdx = self.minChild(i)
            if self.heapList[i] > self.heapList[mChildIdx]:
                self.heapList[i], self.heapList[mChildIdx] = self.heapList[mChildIdx], self.heapList[i]
            # swich the position and check its child again
            i = mChildIdx

    def minChild(self, i):
        # get the smaller child of node i
        if i*2+1 > self.curSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        # move last to the front
        self.heapList[1] = self.heapList[self.curSize]
        self.curSize -= 1
        self.heapList.pop()

        # move last down
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
    biHeap = MinBinaryHeap()
    arr = []
    for _ in range(10):
        arr.append(random.randint(1,100))
        # biHeap.insert(random.randint(1,50))
    print(arr)
    # for num in arr:
    #     biHeap.insert(num)
    biHeap.buildHeap(arr)
    print(biHeap.heapList)
    minNum = biHeap.delMin()
    print(biHeap.heapList)
    print(minNum)

if __name__ == "__main__":
    main()

