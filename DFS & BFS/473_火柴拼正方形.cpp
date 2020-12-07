#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    private:
    bool dfs(vector<int>& nums, vector<int>& edges, int index, int target) {
        if (nums.size() == index) {
            return edges[0] == edges[1] && edges[1] == edges[2] &&
                   edges[2] == edges[3];
        }
        for (int i = 0; i < 4; i++) {
            if (edges[i] + nums[index] > target) {
                continue;
            }
            edges[i] += nums[index];
            if (dfs(nums, edges, index + 1, target)) {
                return true;
            }
            edges[i] -= nums[index];
        }
        return false;
    }

    public:
    bool makesquare(vector<int>& nums) {
        if (nums.size() < 4) {
            return false;
        }
        int sum = 0;
        for (auto& num : nums) {
            sum += num;
        }
        if (sum % 4) {
            return false;
        }
        vector<int> edges(4, 0);
        sort(nums.begin(), nums.end(),
             [](int x, int y) -> bool { return y < x; });
        return dfs(nums, edges, 0, sum / 4);
    }
};
