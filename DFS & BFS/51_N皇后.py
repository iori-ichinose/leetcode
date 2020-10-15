class Solution:
    '''
    def solveNQueens(self, n: int) -> list:
        ans = list()
        res = [['.'] * n for i in range(n)]

        def isValid(row: int, col: int):
            for i in range(row):
                if res[i][col] == 'Q':
                    return False

            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if res[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if res[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            return True

        def dfs(floor):
            if floor == n:
                ans.append([''.join(row) for row in res])

            for i in range(n):
                if isValid(floor, i):
                    res[floor][i] = 'Q'
                    dfs(floor + 1)
                    res[floor][i] = '.'

        dfs(0)
        return ans
    '''

    def solveNQueens(self, n: int) -> list:
        ans = list()
        res = [['.'] * n for i in range(n)]
        col, diag, reverse_diag = [False] * n, [False] * 2 * n, [False] * 2 * n

        def dfs(floor: int):
            if floor == n:
                ans.append([''.join(row) for row in res])
                return

            for i in range(n):
                if not col[i] and not diag[floor + i] and not reverse_diag[n - floor + i]:
                    res[floor][i] = 'Q'
                    col[i], diag[floor + i],
                    reverse_diag[n - floor + i] = True, True, True
                    dfs(floor + 1)
                    res[floor][i] = '.'
                    col[i], diag[floor + i],
                    reverse_diag[n - floor + i] = False, False, False

        dfs(0)
        return ans
