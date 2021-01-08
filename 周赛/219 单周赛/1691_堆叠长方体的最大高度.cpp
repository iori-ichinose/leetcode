#include <vector>
using namespace std;

class Solution {
  public:
    int maxHeight(vector<vector<int>>& cuboids) {
        int n = cuboids.size();
        for (auto& cub : cuboids) {
            sort(cub.begin(), cub.end());
        }

        sort(cuboids.begin(), cuboids.end(),
             [](const vector<int>& v1, const vector<int>& v2) -> bool {
                 if (v1[2] != v2[2]) {
                     return v1[2] < v2[2];
                 } else {
                     return v1[0] + v1[1] < v2[0] + v2[1];
                 }
             });
        int         res = -1;
        vector<int> dp(n, 0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (cuboids[j][0] <= cuboids[i][0] &&
                    cuboids[j][1] <= cuboids[i][1]) {
                    dp[i] = max(dp[i], dp[j]);
                }
            }
            dp[i] += cuboids[i][2];
            res = max(res, dp[i]);
        }

        return res;
    }
};
