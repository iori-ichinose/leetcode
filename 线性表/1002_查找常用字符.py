from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        chars = set(A[0])
        res = []
        for c in chars:
            counts = [word.count(c) for word in A]
            tmp = [c] * min(counts)
            res += tmp

        return res
