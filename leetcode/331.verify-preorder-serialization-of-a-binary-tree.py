#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def traverse(self,sl):
        if not sl:
            return False
        x=sl.pop(0)
        if x=='#':
            return True
        if not self.traverse(sl):
            return False
        if not self.traverse(sl):
            return False
        return True

    def isValidSerialization(self, preorder):
        po=preorder.split(',')
        if not self.traverse(po):
            return False
        return not po

    def isValidSerializationStraight(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        null_nodes = 1
        for node in nodes:
            if node == "#":
                null_nodes -= 1
            else:
                null_nodes += 1
                if null_nodes == 1:
                    return False
        return null_nodes==0


# @lc code=end

