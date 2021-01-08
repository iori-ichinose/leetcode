#include <vector>
using namespace std;

class Solution {
  public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }

        auto dp = new int[n];
        dp[0]   = nums[0];
        for (int i = 1; i < n; i++) {
            int curr = dp[i - 1];
            for (int j = i - 2; j >= i - k && j >= 0; j--) {
                curr = max(curr, dp[j]);
                if (nums[j] > 0) {
                    break;
                }
            }
            dp[i] = curr + nums[i];
        }

        return dp[n - 1];
    }
};