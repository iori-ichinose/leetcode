#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    private:
    bool isValid(string s, unordered_set<string>& words) {
        if (!s.size()) return true;
        for (int i = 1; i <= s.size(); i++) {
            if (words.count(s.substr(0, i)) && isValid(s.substr(i), words))
                return true;
        }
        return false;
    }

    public:
    string longestWord(vector<string>& words) {
        unordered_set<string> allWords(words.begin(), words.end());
        sort(words.begin(), words.end(), [](string& s1, string& s2) -> bool {
            return s1.size() == s2.size() ? s1 < s2 : s1.size() > s2.size();
        });

        for (auto& word : words) {
            allWords.erase(word);
            if (isValid(word, allWords)) {
                return word;
            }
            allWords.insert(word);
        }
        return "";
    }
};
