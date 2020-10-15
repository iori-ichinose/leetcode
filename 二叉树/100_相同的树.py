# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归实现
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q == None and p == None:
            return True
        elif q == None or p == None:
            return False
        elif q.val != p.val:
            return False
        else:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
