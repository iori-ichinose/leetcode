#include <vector>
using namespace std;

class Solution {
  public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) {
            return n;
        }
        int curr = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] != nums[curr - 1]) {
                nums[curr++] = nums[i];
            }
        }
        return curr;
    }
};
