from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        counts = dict()
        if not root:
            return []

        def dfs(root: TreeNode):
            if not root:
                return
            if root.val in counts:
                counts[root.val] += 1
            else:
                counts[root.val] = 1

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        count = max(counts.values())
        return [key for key in counts.keys() if counts[key] == count]
