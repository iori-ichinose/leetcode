# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if not node:
                return
            if node.val == target.vel:
                self.res = node
            dfs(node.left)
            dfs(node.right)

        dfs(cloned)
        return self.res
'''


# 进阶要求
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None
        if target is original:
            return cloned

        lret = self.getTargetCopy(original.left, cloned.left, target)
        if lret:
            return lret
        rret = self.getTargetCopy(original.right, cloned.right, target)
        if rret:
            return rret

        return None
