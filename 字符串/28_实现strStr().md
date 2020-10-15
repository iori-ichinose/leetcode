# 28. 实现strStr()

## [原题](https://leetcode-cn.com/problems/implement-strstr/)

实现 strStr() 函数。

给定一个`haystack`字符串和一个`needle`字符串，在`haystack`字符串中找出`needle`字符串出现的第一个位置 (从0开始)。如果不存在，则返回-1。

## 解题思路

通过暴力遍历依次比较可以得到结果，但是效率太低。在实现时，实际上如果匹配的长度在某处截断，则截断前的一部分不需要再次进行比较，所以可以节省很多时间。譬如`haystack = 'abababcbc', needle = 'ababc'`，后者匹配到第五位时发现并不匹配，但此时不需要从第二位开始重新对比，只需要从第三位开始对比，即可得到正确结果`2`。过程中，应当回溯`重叠字符数-1`个字符。如果重复字符数即为`needle`长度，直接返回开头的字符的index即可。

## 代码实现

```Python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

不好意思放错了。~~人生苦短我用Python~~

```Python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, l = len(haystack), len(needle)
        if l == 0:
            return 0
        if n == 0:
            return -1

        ptr = 0 # haystack的指针
        while ptr < n - l + 1:
            # 寻找到第一个重合的字符
            while ptr < n - l + 1 and haystack[ptr] != needle[0]:
                ptr += 1

            # 记录重合的字符数，从而方便回溯cur_len - 1
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
```
