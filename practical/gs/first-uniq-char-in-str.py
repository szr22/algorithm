import sys

s = 'aiouhdfbaehvahgauuiydgabeh'
def firstUniqCharInStr(s):
    charMap = {}
    for idx, c in enumerate(s):
        if c in charMap:
            charMap[c] = -1
        else:
            charMap[c] = idx
        print(charMap)
    res = sys.maxsize
    
    for c, idx in charMap.items():
        if idx>=0:
            res = min(res, idx)
    return res


res = firstUniqCharInStr(s)
print(res)