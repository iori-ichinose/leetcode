#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
  public:
    int countPairs(vector<int>& deliciousness) {
        unordered_map<int, int> count;

        constexpr int mod = 1000000007;
        int           res = 0;
        int           n   = deliciousness.size();

        for (auto& num : deliciousness) {
            int power = 1;
            for (int i = 0; i <= 21; i++) {
                if (power >= num) {
                    res = (res + count[power - num]) % mod;
                }
                power *= 2;
            }
            count[num]++;
        }
        return res;
    }
};