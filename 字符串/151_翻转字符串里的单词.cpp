#include <deque>
#include <string>
using namespace std;

class Solution {
  public:
    string reverseWords(string s) {
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') {
            left++;
        }
        while (left <= right && s[right] == ' ') {
            right--;
        }

        deque<string> words;
        string        word;

        while (left <= right) {
            char ch = s[left];
            if (!word.empty() && ch == ' ') {
                words.push_front(move(word));
                word = "";
            } else if (ch != ' ') {
                word += ch;
            }
            left++;
        }
        words.push_front(move(word));
        string res;
        while (!words.empty()) {
            res.append(words.front());
            words.pop_front();
            if (!words.empty()) {
                res += ' ';
            }
        }
        return res;
    }
};