#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); i++) {
            auto find = hashtable.find(target - nums[i]);
            if (find != hashtable.end()) {
                return { i, find->second };
            } else {
                hashtable[nums[i]] = i;
            }
        }
        return {};
    }
};

int main() {
    auto        s = Solution();
    vector<int> v = { 2, 7, 11, 15 };
    for (auto n : s.twoSum(v, 9)) {
        cout << n << ' ';
    }
}