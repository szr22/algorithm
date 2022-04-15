# 23280666006931
import re
import collections
from collections import defaultdict
# import string

def retrieveMostFrequentlyUsedWords(helpText, wordsToExclude):
    # remove all special char
    # helpText = re.sub('[\'\".]', ' ', helpText)
    helpText = re.sub('[^A-Za-z ]+', ' ', helpText).lower()

    # parse text to words
    words = helpText.split()


    # count help words
    wordCounter = defaultdict(int)
    wordList = []
    maxCounter = 0
    for word in words:
        if word not in wordsToExclude:
            wordList.append(word)
            wordCounter[word] += 1
            maxCounter = max(maxCounter, wordCounter[word])

    # return
    res = []
    for k, v in wordCounter.items():
        if v == maxCounter:
            res.append(k)
    print(res)

    # print(heapq.heappop(wordCounter.items()))

retrieveMostFrequentlyUsedWords("Jack and   ' Jill. Jack's jill's thh", ['and'])

s = "Jack and Jill. \"Jack's\" jill's thh"
print(re.sub("[' \" ]", " ", s))


arr = [2,2,3,5,4,9,6,7,8]

dup = 0
for i in range(len(arr)):
    dup = dup^arr[i]^i

print(dup)