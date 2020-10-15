from typing import List

# https://leetcode-cn.com/problems/rotate-image
# 给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
#
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 行列对调然后翻转
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for line in matrix:
            line.reverse()
