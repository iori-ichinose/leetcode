class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hash = {}
        for index, num in enumerate(nums):
            hash[num] = index
        for index, num in enumerate(nums):
            j = hash.get(target - num)
            if j != index and j != None:
                return [index, j]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
