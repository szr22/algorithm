import re
import string

my_str = "hey th~!ere"
my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', '', my_str)
print(my_new_string)

my_str = "hey th~!ere"

chars = re.escape(string.punctuation)
print(re.sub(r'['+chars+']', ' ',my_str).split())

paragraph = "Bob hit a ball,,,,,, the hit BALL's flew123 fa23r after it was hit."
paragraph = re.sub('[^a-z0-9]+', ' ', paragraph.lower())
print(paragraph)

regex = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(.\w{2,3})+$'
email = 'ank.itrai-3@26.com.cn'

if(re.search(regex,email)):
    print("Valid Email")
else:
    print("Invalid Email")


def binarySearch(arr, l, r, tar):
    while l <= r:
        mid = (l+r-1)//2

        if arr[mid] == tar:
            return mid
        if arr[mid] < tar:
            l = mid+1
        else:
            r = mid-1
    return -1

def binarySearchRec(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        return -1


def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        pq = PriorityQueue()
        for f_id in self.friends_map[userId]:
            for t_info in self.tweets_map[f_id]:
                if pq.qsize()>0 and pq.queue[0][0]<t_info[0] and pq.qsize()>self.capacity:
                    break
                pq.put(t_info)
                if pq.qsize()>self.capacity:
                    pq.get()
        while pq.queue:
            res.insert(0, pq.get()[1])

        return res