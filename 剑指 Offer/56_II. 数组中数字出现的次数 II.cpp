#include <algorithm>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
  public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int count = 0;
            int bit   = 1 << i;
            for (auto& n : nums) {
                if (n & bit) {
                    count++;
                }
            }

            if (count % 3) {
                res |= bit;
            }
        }
        return res;
    }
};