class Radix:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    #  A utility function to get maximum value in arr[] 
    def getMax(self):
        mx = self.arr[0]
        for i in range(1, self.n):
            if self.arr[i]>mx:
                mx = self.arr[i]
        return mx

    #  A function to do counting sort of arr[] according to 
    #  the digit represented by exp. (e.g. 300 is represented by 100)
    def countSort(self, exp):
        output = [0] * self.n
        count = [0 for _ in range(10)]
        for i in range(self.n):
            count[(self.arr[i]//exp)%10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(self.n-1, -1, -1):
            output[count[(self.arr[i]//exp)%10]-1] = self.arr[i]
            count[(self.arr[i]//exp)%10] -= 1
        for i in range(self.n):
            self.arr[i] = output[i]        

    def radixsort(self):
        m = max(self.arr)
        exp = 1
        while m//exp>0:
            self.countSort(exp)
            exp *= 10

    def __str__(self):
        return (', ').join(list(map(str, self.arr)))

def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix = Radix(arr)
    radix.radixsort()
    print(radix)

if __name__ == "__main__":
    main()