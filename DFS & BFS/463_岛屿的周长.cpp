#include <vector>
using namespace std;

class Solution {
  private:
    vector<pair<int, int>> d = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int                    row, col;

    int dfs(int x, int y, vector<vector<int>>& grid) {
        if (x < 0 || x >= row || y < 0 || y >= col || grid[x][y] == 0) {
            return 1;
        }

        if (grid[x][y] == 2) {
            return 0;
        }

        grid[x][y] = 2;
        int res    = 0;
        for (auto& dn : d) {
            res += dfs(x + dn.first, y + dn.second, grid);
        }
        return res;
    }

  public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int ans = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j]) {
                    ans += 4;
                    if (i && grid[i - 1][j]) {
                        ans -= 2;
                    }
                    if (j && grid[i][j - 1]) {
                        ans -= 2;
                    }
                }
            }
        }
        return ans;
    }

    int islandPerimeter_dfs(vector<vector<int>>& grid) {
        row = grid.size(), col = grid[0].size();
        int ans = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    ans += dfs(i, j, grid);
                }
            }
        }
        return ans;
    }
};
