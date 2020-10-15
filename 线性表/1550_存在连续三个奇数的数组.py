from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        total = 0
        for num in arr:
            if num & 1:
                total += 1
                if total == 3:
                    return True
            else:
                total = 0

        return False
