class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [0] * n
        diags_1 = [0] * (2 * n - 1)  # 正对角线方向
        diags_2 = [0] * (2 * n - 1)  # 反对角线方向
        self.cnt = 0

        def get_res(i):
            if i == n:
                self.cnt += 1
                return
            for j in range(n):
                if cols[j] or diags_1[i - j] or diags_2[i + j]:
                    continue
                cols[j] = diags_1[i - j] = diags_2[i + j] = 1
                get_res(i + 1)
                cols[j] = diags_1[i - j] = diags_2[i + j] = 0  # 回溯
        get_res(0)
        return self.cnt
