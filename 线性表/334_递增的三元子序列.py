from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = 2147483647, 2147483647
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False
