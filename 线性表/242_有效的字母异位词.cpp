#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
    public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> counter;

        for (int i = 0; i < s.size(); i++) {
            counter[s[i]]++;
            counter[t[i]]--;
        }
        for (auto i : counter) {
            if (i.second) return false;
        }
        return true;
    }
};

int main() {
    Solution s;
    bool     ch = s.isAnagram("anagram", "nagaram");
    return 0;
}