# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if not root:
                return

            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root
