

def init():
    with open('word-jump-test-input.txt') as f:
        pair_num = int(f.readline())
        for i in range(pair_num):
            pair = (f.readline().strip(), f.readline().strip())
            pairs.append(pair)
        dict_num = int(f.readline())
        for i in range(dict_num):
            word_dict.add(f.readline().strip())

def word_jump(pair):
    if len(pair[0]) != len(pair[1]):
        return 0
    if pair[0] not in word_dict or pair[1] not in word_dict:
        return 0
    visited = set()
    cur_visit_path = {
        pair[0]: [[pair[0]]]
    }
    while len(cur_visit_path) > 0:
        next_visit_path = {}
        for cur_word, cur_path in cur_visit_path.items():
            visited.add(cur_word)
            next_valid_words = check(cur_word, cur_path, visited)
            for next_word, next_path in next_valid_words.items():
                if next_word in next_visit_path:
                    next_visit_path[next_word] += next_path
                else:
                    next_visit_path[next_word] = next_path
        if pair[1] in next_visit_path:
            return next_visit_path[pair[1]]
        else:
            cur_visit_path = next_visit_path
    return 0

def check(cur_word, cur_path, visited):
    res = {}
    for word in word_dict:
        if word in visited:
            continue
        if len(word) == len(cur_word):
            count = 0
            for i in range(len(word)):
                if word[i] != cur_word[i]:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                tmp = []
                for p in cur_path:
                    tmp.append(p+[word])
                res[word] = tmp
    return res

if __name__ == "__main__":
    word_dict = set()
    pairs = []
    init()
    # print(len(word_dict))
    # print(pairs)
    # res = word_jump(('hit', 'cog'))
    # print(res)
    for pair in pairs:
        res = word_jump(pair)
        print(res)