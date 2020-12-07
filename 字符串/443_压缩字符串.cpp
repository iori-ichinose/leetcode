#include <string>
#include <vector>
using namespace std;

class Solution {
  public:
    int compress(vector<char>& chars) {
        int len = 0;
        for (int i = 0, count = 1; i < chars.size(); i++, count++) {
            if (i == chars.size() - 1 || chars[i] != chars[i + 1]) {
                chars[len++] = chars[i];
                if (count > 1) {
                    for (char ch : to_string(count)) {
                        chars[len++] = ch;
                    }
                }
                count = 0;
            }
        }
        return len;
    }
};
