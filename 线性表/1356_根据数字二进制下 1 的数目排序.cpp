#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> sortByBits(vector<int>& arr) {
        auto get = [](int n) -> int {
            int res = 0;
            while (n) {
                res += n & 1;
                n >>= 1;
            }
            return res;
        };
        vector<int> count(10001);
        for (auto& n : arr) {
            count[n] = get(n);
        }
        sort(arr.begin(), arr.end(), [&count](int x, int y) {
            if (count[x] != count[y]) {
                return count[x] < count[y];
            } else {
                return x < y;
            }
        });
        return arr;
    }
};
