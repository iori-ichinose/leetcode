class Solution:
    def minHeightShelves(self, books: list, shelf_width: int) -> int:
        n = len(books)
        dp = [1000000] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width, cur_book, cur_height = 0, i, 0
            while cur_book > 0:
                width += books[cur_book - 1][0]
                if width > shelf_width:
                    break
                cur_height = max(cur_height, books[cur_book - 1][1])
                dp[i] = min(dp[i], dp[cur_book - 1] + cur_height)
                cur_book -= 1

        return dp[-1]
