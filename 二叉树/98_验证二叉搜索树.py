class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''递归中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        i = 0
        flag = True

        def InOrder(root: TreeNode, vec: list):
            if not root:
                return
            InOrder(root.left, vec)
            vec.append(root.val)
            nonlocal i
            if i and root.val <= vec[i - 1]:
                nonlocal flag
                flag = False
                return
            i += 1
            InOrder(root.right, vec)

        InOrder(root, [])
        return flag
'''

'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        vec = []
        pre = float('-inf')
        while root or vec:
            while root:
                vec.append(root)
                root = root.left
            root = vec.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = float('-inf')

        def InOrder(root: TreeNode):
            if not root:
                return True

            if not InOrder(root.left):
                return False

            if root.val <= self.pre:
                return False
            self.pre = root.val

            return InOrder(root.right)

        return InOrder(root)


s = Solution()
t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)

print(s.isValidBST(t))
