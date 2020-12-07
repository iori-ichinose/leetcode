#include <algorithm>
#include <vector>
using namespace std;

class Solution {
  public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size(), i;
        for (i = n - 2; i >= 0 && nums[i] >= nums[i + 1]; i--)
            ;
        if (i >= 0) {
            int j;
            for (j = n - 1; j >= 0 && nums[i] >= nums[j]; j--)
                ;
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};