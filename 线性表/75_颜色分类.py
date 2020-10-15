from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lf, rt = 0, len(nums) - 1
        i = 0
        while i <= rt:
            while i <= rt and nums[i] == 2:
                nums[i], nums[rt] = nums[rt], nums[i]
                rt -= 1
            if nums[i] == 0:
                nums[i], nums[lf] = nums[lf], nums[i]
                lf += 1
            i += 1
