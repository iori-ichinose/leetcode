from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        bottom, top = 0, len(nums) - 1
        while bottom < top:
            mid = (bottom + top) // 2
            if nums[mid] == nums[mid - 1]:
                if (bottom - mid) % 2:
                    bottom = mid + 1
                else:
                    top = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if (top - mid) % 2:
                    top = mid - 1
                else:
                    bottom = mid + 2
            else:
                return nums[mid]

        return nums[top]

    def singleNonDuplicate_2(self, nums: List[int]) -> int:
        bottom, top = 0, len(nums) - 1

        while bottom < top:
            mid = bottom + (bottom - top) // 2
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                bottom = mid + 2
            else:
                top = mid

        return nums[bottom]
