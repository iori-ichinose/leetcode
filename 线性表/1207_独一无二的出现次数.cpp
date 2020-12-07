// https://leetcode-cn.com/problems/unique-number-of-occurrences/
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> counter;
        unordered_set<int>      member;
        for (auto& num : arr) {
            counter[num]++;
        }
        for (auto& count : counter) {
            member.insert(count.second);
        }
        return member.size() == counter.size();
    }
};
