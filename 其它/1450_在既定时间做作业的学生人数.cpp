// https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time/
// 真正的简单题.jpg

#include <vector>
using namespace std;

class Solution {
    public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime,
                    int queryTime) {
        int res(0);
        for (int i = 0; i < startTime.size(); i++) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
                res++;
            }
        }
        return res;
    }
};
