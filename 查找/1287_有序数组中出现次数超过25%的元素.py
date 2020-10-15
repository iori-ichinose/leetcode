class Solution:
    def findSpecialInteger(self, arr: list) -> int:
        n = len(arr)
        cut = n // 4
        for i in range(n - cut):
            # 如果一个元素数量大于1/4，则n/4后数组元素应当和它相等。
            if arr[i] == arr[i + cut]:
                return arr[i]

        return -1
