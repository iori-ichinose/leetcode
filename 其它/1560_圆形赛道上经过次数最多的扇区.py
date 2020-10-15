# https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track/
# 需要注意的是因为中间部分都是重复走过，对经过次数的贡献相同，因此我们只需要考虑首尾
# 如果 首=尾 则首尾对应的赛道走过的最多
# 如果 首<尾 有可能是中间只走了一次，也有可能走了多次，但必然是中间走的最多。
# 如果 首>尾 说明完全经过中间走了一圈但没超过起点，次数最多的应当是除去终点到起点的余下部分。
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start == end:
            return [start]
        elif start < end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))
