from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a_min, a_max = min(arr), max(arr)
        n = len(arr)
        nums = set(arr)
        sep = (a_max - a_min) // (n - 1)
        for i in range(n - 1):
            if arr[i] != a_max and arr[i] + sep not in nums:
                return False

        return True

    def canMakeArithmeticProgression_2(self, arr: List[int]) -> bool:
        arr.sort()
        sep = arr[1] - arr[0]

        for i in range(2, _ := len(arr)):
            if arr[i] - arr[i - 1] != sep:
                return False

        return True


s = Solution()
arr = [3, 5, 1]

f = s.canMakeArithmeticProgression(arr)
print(f)
