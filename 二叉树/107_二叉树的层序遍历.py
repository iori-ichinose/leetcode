# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 其实就是BFS。
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []
        res = []

        d = list()
        d.append(root)
        while d:
            level = []
            n = len(d)
            for _ in range(n):
                node = d.pop(0)
                level.append(node.val)

                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(level)

        return res[::-1]
