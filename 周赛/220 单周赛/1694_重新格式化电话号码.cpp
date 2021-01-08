#include <string>
using namespace std;

class Solution {
  public:
    string reformatNumber(string number) {
        int    n = number.size(), count = 0;
        string res;

        for (int i = 0; i < n; i++) {
            if (number[i] != ' ' && number[i] != '-') {
                res.push_back(number[i]);
                count++;
                if (count % 3 == 0 && count != 0) {
                    res.push_back('-');
                }
            }
        }
        if (res.back() == '-') {
            res.pop_back();
        } else if (*(res.end() - 2) == '-') {
            res.erase(res.end() - 2);
            res.insert(res.end() - 2, '-');
        }

        return res;
    }
};
