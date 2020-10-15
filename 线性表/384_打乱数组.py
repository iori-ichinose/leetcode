import random


class Solution:
    def __init__(self, nums: list):
        self.nums = nums
        self.ori = nums[:]

    def reset(self) -> list:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.ori[:]
        return self.nums

    def shuffle(self) -> list:
        """
        Returns a random shuffling of the array.
        """
        # random.shuffle(self.nums)
        # 洗牌算法：从之后的元素随机抽取一个与当前元素交换
        for i in range(len(self.nums)):
            swap = random.randint(i, len(self.nums))
            self.nums[i], self.nums[swap] = self.nums[swap], self.nums[i]

        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
