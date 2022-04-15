from collections import Counter

def count_dup(numbers):
    numbers_cnt = Counter(numbers)
    total_count = 0
    for num, cnt in numbers_cnt.items():
        if cnt>1:
            total_count += 1
    print(total_count)


count_dup([1,3,3,4,4,4])