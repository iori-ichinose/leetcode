from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()

        part1 = (a ** last) % 1337
        part2 = (self.superPow(a, b) ** 10) % 1337

        return (part1 * part2) % 1337
