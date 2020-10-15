from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # DFS
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        sums = []
        counts = []

        def dfs(root: TreeNode, level: int) -> None:
            if not root:
                return
            if level < len(sums):
                sums[level] += root.val
                counts[level] += 1
            else:
                sums.append(root.val)
                counts.append(1)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        return [total / count for total, count in zip(sums, count)]

    # BFS
    def averageOfLevels_2(self, root: TreeNode) -> List[float]:
        d = [root]
        res = list()
        while d:
            level = 0
            n = len(d)
            for _ in range(n):
                node = d.pop(0)
                level += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(level / n)

        return res
