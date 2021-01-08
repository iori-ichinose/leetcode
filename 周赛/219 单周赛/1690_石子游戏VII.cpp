#include <vector>
using namespace std;

class Solution {
  public:
    int stoneGameVII(vector<int>& stones) {
        int n = stones.size();
        if (n == 1) {
            return stones[0];
        }
        // dp[i][j] 表示从i到j个石头二者的差值
        // prev[i+1] 表示前i个石头之和
        vector<vector<int>> dp(n, vector<int>(n, 0));
        vector<int>         prev(n + 1);
        for (int i = 0; i < n; i++) {
            prev[i + 1] = prev[i] + stones[i];
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (j - i == 1) {
                    dp[i][j] = max(stones[i], stones[j]);
                } else {
                    dp[i][j] = max(prev[j + 1] - prev[i + 1] - dp[i + 1][j],
                                   prev[j] - prev[i] - dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
};
