class Solution:
    # 转为字符串的解法
    '''
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    '''

    # 不需要转换字符串的解法
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while rev < x:
            rev += 10 * rev + x % 10
            x //= 10
        return rev == x or rev // 10 == x
