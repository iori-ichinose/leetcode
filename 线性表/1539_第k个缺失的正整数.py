from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count, curr, ptr = 0, 1, 0

        while count < k:
            if arr[ptr] == curr:
                if ptr + 1 < len(arr):
                    ptr += 1
            else:
                count += 1
                miss = curr
            curr += 1

        return miss
