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
