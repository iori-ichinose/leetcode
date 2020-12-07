#include <vector>
using namespace std;

class Solution {
  public:
    int minCostToMoveChips(vector<int>& position) {
        int odd(0), even(0);
        for (auto n : position) {
            if (n & 1) {
                odd++;
            } else {
                even++;
            }
        }
        return odd < even ? odd : even;
    }
};
