#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s1, s2;
        vector<int>        res;
        for (auto n : nums1) {
            s1.insert(n);
        }
        for (auto n : nums2) {
            s2.insert(n);
        }
        for (auto n : s1) {
            if (s2.find(n) != s2.end()) {
                res.push_back(n);
            }
        }
        return res;
    }
};
