#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<int, char> dict;
        for (int i = 0; i < order.size(); i++) {
            dict[order[i]] = i;
        }

        for (int i = 0; i < words.size() - 1; i++) {
            string &word1 = words[i], &word2 = words[i + 1];
            bool    flag = false;
            int     n1 = word1.size(), n2 = word2.size(), size = min(n1, n2);
            for (int j = 0; j < size; j++) {
                if (word1[j] != word2[j]) {
                    flag = true;
                    if (dict[word1[j]] > dict[word2[j]]) {
                        return false;
                    }
                    break;
                }
            }
            if (!flag && n1 > n2) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution       s;
    vector<string> v = { "app", "apple" };
    cout << s.isAlienSorted(v, "abcdefghijklmnopqrstuvwxyz");
}