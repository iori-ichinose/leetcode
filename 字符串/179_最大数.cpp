#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
  public:
    string largestNumber(vector<int>& nums) {
        int            n = nums.size();
        vector<string> str_v(n);
        string         res;
        for (int i = 0; i < n; i++) {
            str_v[i] = to_string(nums[i]);
        }

        sort(str_v.begin(), str_v.end(),
             [](string& x, string& y) -> bool { return x + y > y + x; });
        if (str_v[0] == "0") {
            return "0";
        }

        for (auto& s : str_v) {
            res += s;
        }
        return res;
    }
};
