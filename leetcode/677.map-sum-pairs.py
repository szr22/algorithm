#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        target_node = self.trie.search(prefix)
        return target_node.val if target_node else 0


class TrieNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(None, 0)
        self.recorded_dict = {}

    def insert(self, word, val) -> None:
        val_copy = val
        if word in self.recorded_dict:
            val -= self.recorded_dict[word]
        self.recorded_dict[word] = val_copy

        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char, val)
            else:
                cur_node.children[char].val += val
            cur_node = cur_node.children[char]

        cur_node.is_end = True

    def search(self, prefix) -> TrieNode:
        cur_node = self.root
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return None
        return cur_node

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

