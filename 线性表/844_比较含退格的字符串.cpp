#include <stack>
#include <string>
using namespace std;

class Solution {
    public:
    bool backspaceCompare(string S, string T) {
        stack<char> s1, s2;
        auto        func = [](stack<char>& s, char ch) -> void {
            if (ch != '#') {
                s.push(ch);
            } else if (!s.empty()) {
                s.pop();
            }
        };

        for (auto c : S) {
            func(s1, c);
        }
        for (auto c : T) {
            func(s2, c);
        }
        return s1 == s2;
    }
};

int main() {
    Solution s;
    auto     ch = s.backspaceCompare("y#fo##f", "y#f#o##f");
}