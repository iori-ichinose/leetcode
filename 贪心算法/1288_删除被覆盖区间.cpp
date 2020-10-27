#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& v1, const vector<int>& v2) -> bool {
                 return v1[0] == v2[0] ? v1[1] > v2[1] : v1[0] < v2[0];
             });
        int count(0), prev(0), end(0);
        for (auto cur : intervals) {
            end = cur[1];
            if (prev < end) {
                count++;
                prev = end;
            }
        }
        return count;
    }
};
