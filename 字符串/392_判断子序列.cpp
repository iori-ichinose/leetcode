#include <string>
using namespace std;

class Solution {
    public:
    bool isSubsequence(string s, string t) {
        if (!s.size()) return true;
        if (!t.size()) return false;
        int count = 0;
        for (auto ch : t) {
            if (ch == s[count] && ++count == s.size()) {
                return true;
            }
        }
        return false;
    }
};
