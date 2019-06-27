import collections
import re
import heapq

class Dict():
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
    def __lt__(self, other):
        if self.val > other.val:
            return True
        elif self.val < other.val:
            return False
        else:
            return self.key > other.key

def top_k_words(text, k):
    text = re.sub('[^\w| ]', '', text)
    text = text.lower()
    words = text.split()
    # print(words)
    # word_conter = collections.Counter(words)
    # print(word_conter)
    # res = word_conter.most_common(k)
    # print(res)
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word].val += 1
        else:
            word_dict[word] = Dict(word, 1)
    word_heap = list(word_dict.values())
    heapq.heapify(word_heap)
    res = []
    for i in range(k):
        tmp = heapq.heappop(word_heap)
        res.append((tmp.key, tmp.val))
    return res


if __name__ == "__main__":
    text = """
    Apple, the Apple logo, and iPhone are trademarks of Apple Inc., registered in the U.S. and other countries. App Store is a service mark of Apple Inc.

    Android, Google Play and the Google Play logo are trademarks of Google Inc.

    Credit Karma, Inc., P.O. Box 520, San Francisco, CA 94104-0520 Copyright © 2008-2019 Credit Karma, Inc. All Rights Reserved. Note: Never share your online banking or Credit Karma passwords with anyone, including us!
    """
    k = 4
    res = top_k_words(text, k)
    print(res)