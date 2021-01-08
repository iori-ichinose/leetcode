/**
 * 旋转数组
 * C++ 8ms(87.06%) 10MB(38.27%)
 */
#include <vector>
using namespace std;

class Solution {
  public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};
