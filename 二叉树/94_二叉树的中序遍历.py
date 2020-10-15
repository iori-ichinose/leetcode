# 就这就这？
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
                continue

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res
