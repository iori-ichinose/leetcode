#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
    int subarraySum(vector<int>& nums, int k) {
        int                     res(0), sum(0);
        unordered_map<int, int> counter;
        counter[0] = 1;
        for (auto m : nums) {
            sum += m;
            if (counter.find(sum - k) != counter.end()) {
                res += counter[sum - k];
            }
            counter[sum]++;
        }
        return res;
    }
};
