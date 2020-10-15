from typing import List
import collections


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(-v % (k + 1) + v for k, v in collections.Counter(answers).items())


s = Solution()
s.numRabbits([0, 0, 1, 1, 1])
