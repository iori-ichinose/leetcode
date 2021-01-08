/**
 * 只出现一次的数字
 * C++ 36ms(67.65%) 16.9MB(47.75%)
 */
#include <vector>
using namespace std;

class Solution {
  public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (auto n : nums) {
            res ^= n;
        }
        return res;
    }
};
