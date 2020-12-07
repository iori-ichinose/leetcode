#include <algorithm>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(),
             [](const auto& x, const auto& y) -> bool {
                 return x[0] > y[0] || (x[0] == y[0] && x[1] < y[1]);
             });
        vector<vector<int>> res;
        for (auto& person : people) {
            res.insert(res.begin() + person[1], person);
        }
        return res;
    }
};
