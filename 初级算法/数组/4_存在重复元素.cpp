/**
 * 存在重复元素
 * C++ 68ms(79.76%) 19.5MB(40.28%)
 */
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
  public:
    bool containsDuplicate(vector<int>&& nums) {
        unordered_set<int> s;
        for (auto n : nums) {
            if (s.find(n) != s.end()) {
                return false;
            } else {
                s.insert(n);
            }
        }
        return true;
    }
};
