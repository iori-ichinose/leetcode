class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, l = len(haystack), len(needle)
        if l == 0:
            return 0
        if n == 0:
            return -1

        ptr = 0
        while ptr < n - l + 1:
            while ptr < n - l + 1 and haystack[ptr] != needle[0]:
                ptr += 1

            cur_len = ptr_l = 0
            while ptr_l < l and ptr < n and haystack[ptr] == needle[ptr_l]:
                ptr += 1
                ptr_l += 1
                cur_len += 1

            if cur_len == l:
                return ptr - l
            else:
                ptr -= cur_len - 1

        return -1
