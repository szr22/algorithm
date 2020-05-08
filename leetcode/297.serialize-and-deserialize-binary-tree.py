#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.ostring = ''

    def serialize(self, root):
        def helper(node):
            if node:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else: res.append("#")

        res = []
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        vals = iter(data.split(','))

        return helper()

    def serializeStraight(self, root):
        if not root:
            return '#'
        queue = [root]
        res = [str(root.val)]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                res.append(str(cur.left.val))
                queue.append(cur.left)
            else:
                res.append('#')

            if cur.right:
                res.append(str(cur.right.val))
                queue.append(cur.right)
            else:
                res.append('#')
        return ','.join(res)


    def deserializeStraight(self, data):
        node_list = data.split(',')
        if node_list[0] == '#':
            return None
        root = TreeNode(int(node_list[0]))
        queue, i = collections.deque([root]), 1
        while queue:
            node = queue.popleft()
            if node_list[i]=='#':
                node.left = None
            else:
                node.left = TreeNode(int(node_list[i]))

            if node_list[i+1]=='#':
                node.right = None
            else:
                node.right = TreeNode(int(node_list[i+1]))
            queue.append(node.left)
            queue.append(node.right)
            i+=2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

