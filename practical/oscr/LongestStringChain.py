def longest_str_chain(words):
    res = 0
    found = set()
    words_set = set(words)
    words.sort(key=len)
    for i in range(len(words)-1, -1, -1):
        word = words[i]
        cur_max = 0
        queue = set()
        queue.add(word)
        while queue:
            cur_max += 1
            tmp = set()
            while queue:
                w = queue.pop()
                found.add(w)
                target = get_one_distance_word(w, words_set, found)
                if target:
                    tmp.add(target)
            queue = tmp
        res = max(res, cur_max)
        if i <= res:
            break
    return res


def get_one_distance_word(word, words_set, found):
    for i in range(len(word)):
        target = word[:i] + word[i+1:]
        if target not in words_set or target in found:
            continue
        return target

words = ["a","b","ba","bca","bda","bdca"]
res = longest_str_chain(words)
print(res)

def longest_str_chain_dfs(words):
    res = 0
    words_set = set(words)
    for word in words:
        res = max(res, dfs(word, words_set))
    return res

def dfs(word, words_set):
    if not word:
        return 0
    if len(word) == 1:
        return 1 if word in words else 0
    if word not in words_set:
        return 0
    max_len = 0
    for i in range(len(word)):
        target = word[:i]+word[i+1:]
        max_len = max(max_len, dfs(target, words_set))
    return max_len+1

words = ["a","b","ba","bca","bda","bdca"]
res = longest_str_chain_dfs(words)
print(res)
