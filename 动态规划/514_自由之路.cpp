#include <cstring>
#include <iterator>
#include <string>
#include <vector>
using namespace std;

class Solution {
  public:
    int findRotateSteps(string ring, string key) {
        int                 n = ring.size(), m = key.size();
        vector<vector<int>> pos(26);
        for (int i = 0; i < n; i++) {
            pos[ring[i] - 'a'].push_back(i);
        }

        int dp[m][n];
        memset(dp, 0x3f3f3f3f, sizeof(dp));
        for (auto& i : pos[key[0] - 'a']) {
            dp[0][i] = min(i, n - i) + 1;
        }

        for (int i = 1; i < m; i++) {
            for (auto j : pos[i - 'a']) {
                for (auto k : pos[key[i - 1] - 'a']) {
                    dp[i][j] =
                      min(dp[i][j],
                          dp[i - 1][k] + min(abs(j - k), n - abs(j - k)) + 1);
                }
            }
        }
        int res = 0x3f3f3f3f;
        for (auto& p : dp) {
            for (auto& n : p) {
                res = min(res, n);
            }
        }

        return res;
    }
};
