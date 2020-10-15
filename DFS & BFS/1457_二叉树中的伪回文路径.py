# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.res = 0

        def isValid(path) -> bool:
            count = 0
            for num in path:
                if num & 1:
                    count += 1
                    if count > 1:
                        return False
            return True

        def dfs(root: TreeNode, count: list):
            if not root:
                return
            count[root.val] += 1
            if not root.left and not root.right and isValid(count):
                self.res += 1
                count[root.val] -= 1
                return
            dfs(root.left, count)
            dfs(root.right, count)
            count[root.val] -= 1

        dfs(root, [0] * 10)
        return self.res
