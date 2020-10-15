from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = dict()
        res = list()
        for num in nums1:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for num in nums2:
            if num in count and count[num]:
                count[num] -= 1
                res.append(num)
        return res

    def intersect_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ptr1, ptr2 = 0, 0
        res = list()
        l1, l2 = len(nums1), len(nums2)

        while ptr1 < l1 and ptr2 < l2:
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1

        return res
