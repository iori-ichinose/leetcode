/**
 * 买卖股票的最佳时机 II
 * C++ 4ms(91.57%), 7.4MB(71.58%)
 */
#include <vector>
using namespace std;

class Solution {
  public:
    int maxProfit(vector<int>& prices) {
        int dp[2] = {0, -prices[0]};
        for (int i = 1; i < prices.size(); i++) {
            dp[0] = max(dp[0], dp[1] + prices[i]);
            dp[1] = max(dp[1], dp[0] - prices[i]);
        }
        return dp[0];
    }
};
