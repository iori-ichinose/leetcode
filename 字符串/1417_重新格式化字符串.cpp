#include <stack>
#include <string>
using namespace std;

class Solution {
  public:
    string reformat(string s) {
        stack<char> digits, letters;
        string      res;
        for (auto ch : s) {
            if (isdigit(ch)) {
                digits.push(ch);
            } else {
                letters.push(ch);
            }
        }
        auto m = digits.size(), n = letters.size();
        if (m > n + 1 || n > m + 1) {
            return "";
        }

        if (m > n) {
            while (!letters.empty()) {
                res.push_back(digits.top());
                res.push_back(letters.top());
                digits.pop();
                letters.pop();
            }
            res.push_back(digits.top());
        } else {
            while (!digits.empty()) {
                res.push_back(letters.top());
                res.push_back(digits.top());
                digits.pop();
                letters.pop();
            }
            if (!letters.empty()) {
                res.push_back(letters.top());
            }
        }
        return res;
    }
};