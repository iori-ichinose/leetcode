#include <string>
#include <unordered_map>
using namespace std;

class Solution {
  public:
    bool CheckPermutation(string s1, string s2) {
        if (s1.size() != s2.size()) {
            return false;
        }

        unordered_map<char, int> counts;
        for (char ch : s1) {
            counts[ch]++;
        }
        for (char ch : s2) {
            counts[ch]--;
            if (counts[ch] < 0) {
                return false;
            }
        }
        return true;
    }
};