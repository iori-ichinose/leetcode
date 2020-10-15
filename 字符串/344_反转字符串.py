# https://leetcode-cn.com/problems/reverse-string/
# 了 转 反
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 不要脸解法：
        # s.reverse()

        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
