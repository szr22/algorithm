class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChile(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not(self.leftChild and self.rightChild)
    
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    
    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree(TreeNode):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, curNode):
        if key < curNode.key:
            if curNode.hasLeftChild():
                self._put(key, val, curNode.leftChild)
            else:
                curNode.leftChild = TreeNode(key, val, parent=curNode)
        else:
            if curNode.hasRightChild():
                self._put(key, val, curNode.rightChild)
            else:
                curNode.rightChild = TreeNode(key, val, parent=curNode)
    
    def __setitem__(self, key, val):
        self.put(key, val)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, curNode):
        if not curNode:
            return None
        elif curNode.key == key:
            return curNode
        elif curNode.key > key:
            return self._get(key, curNode.leftChild)
        else:
            return self._get(key, curNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size > 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    def findSuccessor(self):
        suc = None
        if self.hasRightChild():
            suc = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    suc = self.parent
                else:
                    self.parent.right = None
                    suc = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return suc
    
    def findMin(self):
        cur = self
        while cur.hasLeftChild():
            cur = cur.leftChild
        return cur

    def remove(self, cur):
        if cur.isLeaf():
            if cur == cur.parent.leftChild:
                cur.parent.leftChild = None
            else:
                cur.parent.rightChild = None
        elif cur.hasBothChildren():
            suc = cur.findSuccessor()
            suc.spliceOut()
            cur.key = suc.key
            cur.val = cur.val
        else:
            if cur.hasLeftChild():
                if cur.isLeftChild():
                    cur.leftChild.parent = cur.parent
                    cur.parent.leftChild = cur.leftChild
                elif cur.isRightChild():
                    cur.leftChild.parent = cur.parent
                    cur.parent.rightChild = cur.leftChild
                else:
                    cur.replaceNodeData(
                        cur.leftChild.key,
                        cur.leftChild.val,
                        cur.leftChild.leftChild,
                        cur.leftChild.rightChild
                    )
            else:
                if cur.isLeftisRightChildChild():
                    cur.rightChild.parent = cur.parent
                    cur.parent.leftChild = cur.rightChild
                elif cur.isRightChild():
                    cur.rightChild.parent = cur.parent
                    cur.parent.rightChild = cur.rightChild
                else:
                    cur.replaceNodeData(
                        cur.rightChild.key,
                        cur.rightChild.val,
                        cur.rightChild.leftChild,
                        cur.rightChild.rightChild
                    )

def main():
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"

    print(mytree[6])
    print(mytree[2])

    mytree[1] = "test"
    print(mytree[1])

    del mytree[1]
    print(mytree[1])
    del mytree[1]

if __name__ == "__main__":
    main()