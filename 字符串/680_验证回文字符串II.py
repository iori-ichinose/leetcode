class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        def isValid(start: int, end: int) -> bool:
            tmp = s[start:end + 1]
            return tmp == tmp[::-1]

        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return isValid(low, high - 1) or isValid(low + 1, high)
        return True
