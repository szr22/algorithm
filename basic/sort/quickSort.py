class QuickSort():
    def __init__(self, arr):
        self.arr = arr


def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix = Radix(arr)
    radix.radixsort()
    print(radix)

if __name__ == "__main__":
    main()