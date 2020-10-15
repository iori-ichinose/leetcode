# https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
# 两只蚂蚁相遇时同时转向，就等同于没有转向直接穿过对方。

class Solution:
    def getLastMoment(self, n: int, left: list, right: list) -> int:
        m1 = max(ant for ant in left) if left else 0
        m2 = max(n - ant for ant in right) if right else 0
        return m1 if m1 > m2 else m2
