import sys
from collections import OrderedDict

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.horizon_distance = sys.maxsize

class Solution:
    def bottomView(self, root):
        if not root:
            return None

        horizon_distance = 0
        hashmap = OrderedDict()
        queue = []
        root.horizon_distance = horizon_distance
        queue.append(root)

        while queue:
            tmp = queue.pop(0)
            horizon_distance = tmp.horizon_distance

            hashmap[horizon_distance] = tmp.val

            if tmp.left:
                tmp.left.horizon_distance = horizon_distance-1
                queue.append(tmp.left)

            if tmp.right:
                tmp.right.horizon_distance = horizon_distance+1
                queue.append(tmp.right)

        res = []
        for k, v in sorted(hashmap.items()):
            print(k, v)
            res.append(v)
        return res


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

res = Solution().bottomView(root)
print(res)

# sorted(key_value.items(), key = lambda kv:(kv[1], kv[0]))