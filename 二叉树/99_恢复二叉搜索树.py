# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        stack = []
        pre = None
        x = None
        y = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre and pre.val > root.val:
                y = root
                if x == None:
                    x = pre

            pre = root
            root = root.right

        x.val, y.val = y.val, x.val
