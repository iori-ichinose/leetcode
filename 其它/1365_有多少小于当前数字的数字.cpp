#include <vector>
using namespace std;

class Solution {
    public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int         n = nums.size();
        vector<int> cnt(101, 0), res(n);

        for (int i = 0; i < n; i++) {
            cnt[nums[i]]++;
        }
        for (int i = 1; i <= 100; i++) {
            cnt[i] += cnt[i - 1];
        }

        for (int i = 0; i < n; i++) {
            res[i] = nums[i] == 0 ? 0 : cnt[nums[i] - 1];
        }
        return res;
    }
};