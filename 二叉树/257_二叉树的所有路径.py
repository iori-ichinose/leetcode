# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        paths = list()

        def dfs(root: TreeNode, path: str):
            if not root:
                return
            path += str(root.val)
            # 如果是叶子结点，将当前路径添加到结果中去。
            if not root.left and not root.right:
                paths.append(path)
            # 否则在后面添加'->'，然后递归DFS。
            else:
                path += '->'
                dfs(root.left, path)
                dfs(root.right, path)

        dfs(root, str())
        return paths
