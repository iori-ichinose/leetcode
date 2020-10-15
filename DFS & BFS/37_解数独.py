from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.valid = False
        space = list()
        line = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    space.append((i, j))
                else:
                    x = int(board[i][j]) - 1
                    line[i][x] = col[j][x] = block[i // 3][j // 3][x] = True

        def dfs(pos: int):
            if pos == len(space):
                self.valid = True
                return

            i, j = space[pos]
            for digit in range(9):
                if line[i][digit] == col[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = col[j][digit] = block[i //
                                                           3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = col[j][digit] = block[i //
                                                           3][j // 3][digit] = False
                if self.valid:
                    return

        dfs(0)
