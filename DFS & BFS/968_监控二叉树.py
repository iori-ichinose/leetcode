# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0

        def dfs(node: TreeNode):
            if not node:
                return 0
            lf = dfs(node.left)
            rt = dfs(node.right)
            if lf == rt == 0:
                node.val = 1
            elif lf == 1 or rt == 1:
                node.val = 2
                self.cameras += 1
            else:
                node.val = 0

            return node.val

        dfs(root)
        return self.cameras + int(root.val == 1)
