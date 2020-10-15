from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        tmp = []

        def dfs(root: TreeNode, remain: int):
            if not root:
                return
            tmp.append(root.val)
            if root.val == remain and not root.left and not root.right:
                res.append(tmp[:])
            dfs(root.left, remain - root.val)
            dfs(root.right, remain - root.val)
            tmp.pop()

        dfs(root, sum)
        return res
