#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> sign;
        sign.push(1);
        int ans = 0, num = 0, op = 1;
        for (char c: s) {
            if (c == ' ') continue;
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
                continue;
            }
            ans += op * num;
            num = 0;
            switch (c) {
                case '+': op = sign.top(); break;
                case '-': op = -sign.top(); break;
                case '(': sign.push(op); break;
                case ')': sign.pop();
            }
        }
        ans += op * num;
        return ans;
    }
};