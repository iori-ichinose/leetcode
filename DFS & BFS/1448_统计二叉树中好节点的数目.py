# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root: TreeNode, max_val: int):
            if not root:
                return
            if root.val >= max_val:
                self.res += 1
                max_val = root.val
            dfs(root.left, max_val)
            dfs(root.right, max_val)

        if not root:
            return 0

        dfs(root, root.val)
        return self.res
