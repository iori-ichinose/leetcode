// https://leetcode-cn.com/problems/largest-triangle-area/
// 暴 力 算 法 ！

#include <algorithm>
#include <vector>
using namespace std;
class Solution {
    private:
    inline int mabs(int n) {
        return n > 0 ? n : -n;
    }
    inline double mmax(double a, double b) {
        return a > b ? a : b;
    }

    public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int    n   = points.size();
        double res = 0;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int dx1 = points[j][0] - points[i][0],
                        dx2 = points[k][0] - points[i][0],
                        dy1 = points[j][1] - points[i][1],
                        dy2 = points[k][1] - points[i][1];
                    res     = mmax(res, mabs(dx1 * dy2 - dx2 * dy1) / 2.0);
                }
            }
        }
        return res;
    }
};
