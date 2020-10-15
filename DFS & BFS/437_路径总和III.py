# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum0: int) -> int:
        if not root:
            return 0

        self.count = 0
        m = {0: 1}

        def dfs(root, cur_sum):
            if not root:
                return
            if cur_sum - sum0 in m:
                self.count += m[cur_sum - sum0]

            m[cur_sum] = 1 if cur_sum not in m else m[cur_sum] + 1
            if root.left:
                dfs(root.left, cur_sum + root.left.val)
            if root.right:
                dfs(root.right, cur_sum + root.right.val)
            m[cur_sum] -= 1

        dfs(root, root.val)
        return self.count
