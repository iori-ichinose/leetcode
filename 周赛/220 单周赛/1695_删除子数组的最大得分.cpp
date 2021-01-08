#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
  public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }

        unordered_set<int> s;

        int left(0), right(0), res(0), sum(0);

        while (right < n) {
            if (s.find(nums[right]) == s.end()) {
                sum += nums[right];
                res = max(res, sum);
                s.insert(nums[right]);
                right++;
            } else {
                while (left < right && nums[left] != nums[right]) {
                    sum -= nums[left];
                    s.erase(nums[left]);
                    left++;
                }
                left++, right++;
            }
        }

        return res;
    }
};
