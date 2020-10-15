from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            val = postorder.pop()
            root = TreeNode(val)

            index = inorder.index(val)
            root.right = helper(index + 1, hi)
            root.left = helper(lo, index - 1)

            return root

        return helper(0, len(inorder) - 1)
