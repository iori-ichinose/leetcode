#include <cstring>
#include <queue>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
        vector<vector<int>> res;

        bool visited[R][C];
        memset(visited, 0, sizeof(visited));
        visited[r0][c0] = true;

        queue<vector<int>> q;
        q.push({r0, c0});

        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            res.push_back(cur);
            auto x = cur[0], y = cur[1];
            if (x < R - 1 && !visited[x + 1][y]) {
                q.push({x + 1, y});
                visited[x + 1][y] = true;
            }
            if (x > 0 && !visited[x - 1][y]) {
                q.push({x - 1, y});
                visited[x - 1][y] = true;
            }
            if (y > 0 && !visited[x][y - 1]) {
                q.push({x, y - 1});
                visited[x][y - 1] = true;
            }
            if (y < C - 1 && !visited[x][y + 1]) {
                q.push({x, y + 1});
                visited[x][y + 1] = true;
            }
        }

        return res;
    }
};
