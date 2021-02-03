#include <vector>
using namespace std;

class Solution {
    public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        auto n  = coordinates.size();
        auto ix = coordinates[0][0], iy = coordinates[0][1];
        auto ex = coordinates[n - 1][0], ey = coordinates[n - 1][1];
        for (auto i = 1; i < n - 1; i++) {
            auto x = coordinates[i][0], y = coordinates[i][1];
            if ((x - ix) * (y - ey) != (y - iy) * (x - ex)) {
                return false;
            }
        }
        return true;
    }
};
