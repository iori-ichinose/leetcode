#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    private:
    unordered_map<string, vector<string>> m;

    public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        if (m.find(s) != m.end()) {
            return m[s];
        }
        if (s.empty()) {
            return { "" };
        }
        vector<string> res;
        for (auto word : wordDict) {
            if (s.substr(0, word.size()) != word) {
                continue;
            }
            vector<string>&& tmp = wordBreak(s.substr(word.size()), wordDict);
            for (auto item : tmp) {
                if (!item.empty()) {
                    res.push_back(word + " " + item);
                } else {
                    res.push_back(word);
                }
            }
            m[s] = res;
            return res;
        }
    }
};
