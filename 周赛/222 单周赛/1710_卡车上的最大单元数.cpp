#include <vector>
using namespace std;

class Solution {
  public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(),
             [](const auto& u, const auto& v) -> bool { return u[1] > v[1]; });
        int res = 0;
        for (auto& box : boxTypes) {
            if (box[0] <= truckSize) {
                res += box[0] * box[1];
                truckSize -= box[0];
            } else {
                res += box[1] * truckSize;
                break;
            }
        }
        return res;
    }
};
