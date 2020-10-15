class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** (len(bin(num)) - 2) - num - 1

    def findComplement_2(self, num: int) -> int:
        n, m = 0, num
        while m:
            m >>= 1
            n += 1

        return num ^ ((1 << n) - 1)
