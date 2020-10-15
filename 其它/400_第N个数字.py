class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        length, cnt, i = 0, 9, 1
        while (s := length + cnt * i) < n:
            length = s
            cnt *= 10
            i += 1

        index = (n - length - 1) % i
        num = 10 ** (i - 1) + (n - length - 1) / i
        return int(str(num)[index])
